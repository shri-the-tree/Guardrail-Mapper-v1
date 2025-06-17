import sys
import os
sys.path.append(os.path.abspath(""))  # Ensure project root is on path

import json
from guardrail_mapper.core import GuardrailMapper
from guardrail_mapper.models import Interaction  # ✅ Add this import

# 🔁 Load test inputs
with open("guardrail_mapper/test_inputs.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

interactions = [Interaction(**x) for x in raw]

# 🧠 Run analysis
mapper = GuardrailMapper()
results = mapper.batch_analyze(interactions)

# 📤 Print results
for r in results:
    print(f"{r.inferred_layer:<15} | {r.behavior:<25} | {r.summary}")
    if r.bypass_suggestions:
        print("  🔧 Suggestions:", ", ".join(r.bypass_suggestions))
    print("-" * 90)
