import json
from guardrail_mapper.models import Interaction, AnalysisResult
from .llm_analyst import analyze_with_qwen
from .strategy_mapper import map_strategy
from .obfuscation_mapper import suggest_obfuscation

class GuardrailMapper:
    def __init__(self):
        pass

    def analyze(self, interaction: Interaction) -> AnalysisResult:
        # 🔍 Run classification via Qwen
        analysis = analyze_with_qwen(interaction.prompt, interaction.response, interaction.latency_ms)

        behavior = analysis.get("behavior", "Ambiguous / Other")
        layer = analysis.get("layer", "In-Model")
        summary = analysis.get("summary", "No summary provided.")

        # 🎯 Strategy enrichment
        strategy = map_strategy(behavior, layer)
        bypass_strategy_category = strategy.get("bypass_strategy_category", "")
        attack_strategies = strategy.get("recommended_attack_strategies", [])
        regeneration_instruction = strategy.get("regeneration_instruction", "")

        # 🧪 Obfuscation methods
        obfuscation_methods = suggest_obfuscation(
            layer=layer,
            strategy_category=bypass_strategy_category
        )

        return AnalysisResult(
            prompt=interaction.prompt,
            response=interaction.response,
            latency_ms=interaction.latency_ms,
            behavior=behavior,
            inferred_layer=layer,
            summary=summary,
            bypass_suggestions=analysis.get("bypass_suggestions", []),
            bypass_strategy_category=bypass_strategy_category,
            attack_strategies=attack_strategies,
            obfuscation_methods=obfuscation_methods,
            regeneration_instruction=regeneration_instruction
        )

    def batch_analyze(self, interactions: list[Interaction]) -> list[AnalysisResult]:
        return [self.analyze(i) for i in interactions]

    def export_results(self, results: list[AnalysisResult], path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([r.dict() for r in results], f, indent=2, ensure_ascii=False)
