"""
Auto-AI-Fuzzer: Swagger-to-Attack Automation Tool
Parses OpenAPI/Swagger specs to auto-discover AI endpoints and launch targeted attacks.
"""

import json
import requests
import time
import argparse
import logging
from typing import List, Dict
from dataclasses import dataclass, asdict

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)-8s | %(message)s')
logger = logging.getLogger("AutoFuzzer")

@dataclass
class Endpoint:
    url: str
    method: str

@dataclass
class FuzzResult:
    endpoint_url: str
    method: str
    payload_snippet: str
    status_code: int
    anomaly_detected: bool
    snippet: str

class AutoAIFuzzer:
    def __init__(self, swagger_file: str, payload_file: str) -> None:
        self.swagger_file = swagger_file
        self.payload_file = payload_file
        self.target_host = ""
        self.base_path = ""
        self.ai_endpoints: List[Endpoint] = []
        self.payloads: List[str] = []
        self.results: List[FuzzResult] = []

    def load_files(self) -> bool:
        try:
            with open(self.swagger_file, 'r') as f:
                data = json.load(f)
                self.target_host = data.get("host", "localhost:8000")
                self.base_path = data.get("basePath", "/")
                self._extract_endpoints(data.get("paths", {}))
        except Exception as e:
            logger.error(f"Swagger parse error: {e}")
            return False
            
        try:
            with open(self.payload_file, 'r') as f:
                self.payloads = [line.strip() for line in f if line.strip()]
        except Exception as e:
            logger.error(f"Payload load error: {e}")
            return False
        return True

    def _extract_endpoints(self, paths: Dict) -> None:
        keywords = ["chat", "agent", "prompt", "completion", "llm", "ai"]
        for path, methods in paths.items():
            if any(k in path.lower() for k in keywords):
                for method in methods.keys():
                    if method.lower() in ["get", "post"]:
                        url = f"http://{self.target_host}{self.base_path}{path.lstrip('/')}"
                        self.ai_endpoints.append(Endpoint(url=url, method=method.upper()))
                        logger.info(f"Discovered AI Endpoint: [{method.upper()}] {url}")

    def run_attack(self) -> None:
        if not self.ai_endpoints:
            logger.error("No AI endpoints discovered.")
            return
            
        logger.info(f"Starting fuzzing on {len(self.ai_endpoints)} endpoints...")
        for ep in self.ai_endpoints:
            for payload in self.payloads:
                try:
                    resp = requests.post(ep.url, json={"prompt": payload}, timeout=10) if ep.method == "POST" else requests.get(ep.url, params={"prompt": payload}, timeout=10)
                    anomaly = "password" in resp.text.lower() or "sk-" in resp.text
                    self.results.append(FuzzResult(ep.url, ep.method, payload[:30], resp.status_code, anomaly, resp.text[:100]))
                    if anomaly: logger.warning(f"ANOMALY DETECTED at {ep.url}")
                except Exception as e:
                    logger.error(f"Request failed: {e}")
                time.sleep(1)
        
        self._export_json()

    def _export_json(self) -> None:
        with open("fuzzer_results.json", "w") as f:
            json.dump([asdict(r) for r in self.results], f, indent=2)
        logger.info(f"Fuzzing completed. {len(self.results)} requests sent. Results saved to fuzzer_results.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-AI-Fuzzer")
    parser.add_argument("--swagger", default="test_swagger.json", help="Swagger JSON file")
    parser.add_argument("--payloads", default="payloads.txt", help="Payloads file")
    args = parser.parse_args()
    
    fuzzer = AutoAIFuzzer(args.swagger, args.payloads)
    if fuzzer.load_files():
        fuzzer.run_attack()