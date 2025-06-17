import json
from .models import Interaction, AnalysisResult
from .llm_analyst import analyze_with_qwen

class GuardrailMapper:
    def __init__(self):
        pass

    def analyze(self, interaction: Interaction) -> AnalysisResult:
        analysis = analyze_with_qwen(interaction.prompt, interaction.response, interaction.latency_ms)
        behavior = analysis["behavior"]
        layer = analysis["layer"]
        summary = analysis["summary"]

        return AnalysisResult(
            prompt=interaction.prompt,
            response=interaction.response,
            latency_ms=interaction.latency_ms,
            behavior=behavior,
            inferred_layer=layer,
            summary=summary,  # <-- add comma here
            bypass_suggestions=analysis.get("bypass_suggestions", [])
        )

    def batch_analyze(self, interactions: list[Interaction]) -> list[AnalysisResult]:
        return [self.analyze(i) for i in interactions]

    def export_results(self, results: list[AnalysisResult], path: str):
        with open(path, "w") as f:
            json.dump([r.dict() for r in results], f, indent=2)