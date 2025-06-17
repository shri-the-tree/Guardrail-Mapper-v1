from dataclasses import dataclass

@dataclass
class Interaction:
    prompt: str
    response: str
    latency_ms: int | None = None  # Optional for flexibility

@dataclass
class AnalysisResult:
    prompt: str
    response: str
    latency_ms: int | None
    behavior: str
    inferred_layer: str
    summary: str
    bypass_suggestions: list[str]

    def dict(self):
        return {
            "prompt": self.prompt,
            "response": self.response,
            "latency_ms": self.latency_ms,
            "behavior": self.behavior,
            "inferred_layer": self.inferred_layer,
            "summary": self.summary,
            "bypass_suggestions": self.bypass_suggestions
        }
