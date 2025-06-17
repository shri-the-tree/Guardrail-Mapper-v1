from dataclasses import dataclass
from typing import Optional

@dataclass
class Interaction:
    prompt: str
    response: str
    latency_ms: Optional[int] = None

@dataclass
class AnalysisResult:
    prompt: str
    response: str
    latency_ms: Optional[int]
    behavior: str
    inferred_layer: str
    summary: str
    bypass_suggestions: list[str]
    bypass_strategy_category: Optional[str] = None
    attack_strategies: Optional[list[str]] = None
    obfuscation_methods: Optional[list[str]] = None
    regeneration_instruction: Optional[str] = None

    def dict(self):
        return {
            "prompt": self.prompt,
            "response": self.response,
            "latency_ms": self.latency_ms,
            "behavior": self.behavior,
            "inferred_layer": self.inferred_layer,
            "summary": self.summary,
            "bypass_suggestions": self.bypass_suggestions,
            "bypass_strategy_category": self.bypass_strategy_category,
            "attack_strategies": self.attack_strategies,
            "obfuscation_methods": self.obfuscation_methods,
            "regeneration_instruction": self.regeneration_instruction,
        }
