import json
from guardrail_mapper.models import AnalysisResult

def export_to_mistral_ready(results: list[AnalysisResult], output_path="mistral_ready.json"):
    mistral_data = []

    for r in results:
        mistral_data.append({
            "base_prompt": r.prompt,
            "llm_response": r.response,
            "latency_ms": r.latency_ms,
            "behavior": r.behavior,
            "guardrail_layer": r.inferred_layer,
            "summary": r.summary,
            "bypass_strategy_category": getattr(r, "bypass_strategy_category", "Unknown"),
            "attack_strategies": r.bypass_suggestions,
            "obfuscation_methods": getattr(r, "recommended_obfuscation_methods", []),
            "regeneration_instruction": getattr(r, "regeneration_instruction", "")
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(mistral_data, f, indent=2, ensure_ascii=False)

    print(f"✅ Exported {len(mistral_data)} results to {output_path}")
