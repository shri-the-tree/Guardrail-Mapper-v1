import sys
import os
import json
import time
from dotenv import load_dotenv
from groq import Groq
from guardrail_mapper.core import GuardrailMapper
from guardrail_mapper.models import Interaction
from export_mistral_ready import export_to_mistral_ready

# ✅ Ensure project root is on path
sys.path.append(os.path.abspath(""))

# 🔐 Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in environment. Make sure .env is set.")

client = Groq(api_key=api_key)

# 📥 Load prompts from testcases.json
with open("testcases(10).json", "r", encoding="utf-8") as f:
    test_cases = json.load(f)

model_name = "llama-3.1-8b-instant"

# 📦 Final output for guardrail_mapper input
mapped_inputs = []

for i, prompt in enumerate(test_cases, start=1):
    print(f"\n🧪 Running Test Case {i}...")

    messages = [{"role": "user", "content": prompt}]
    start_time = time.time()

    # Generate response
    completion = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response_text = ""
    for chunk in completion:
        part = chunk.choices[0].delta.content or ""
        print(part, end="", flush=True)
        response_text += part

    elapsed_time_ms = int((time.time() - start_time) * 1000)

    mapped_inputs.append({
        "prompt": prompt,
        "response": response_text.strip(),
        "latency_ms": elapsed_time_ms
    })

    print(f"\n⏱ Latency: {elapsed_time_ms}ms")
    print("-" * 60)

# 💾 Save as test_inputs for analysis
with open("guardrail_mapper/test_inputs.json", "w", encoding="utf-8") as f:
    json.dump(mapped_inputs, f, indent=2, ensure_ascii=False)

print("\n✅ Saved guardrail-compatible input data to 'guardrail_mapper/test_inputs.json'")

# 🔁 Load and analyze with GuardrailMapper
with open("guardrail_mapper/test_inputs.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

interactions = [Interaction(**x) for x in raw]

mapper = GuardrailMapper()
results = mapper.batch_analyze(interactions)

# 📤 Print results
for r in results:
    print(f"{r.inferred_layer:<15} | {r.behavior:<25} | {r.summary}")
    if r.bypass_suggestions:
        print("  🔧 Suggestions:", ", ".join(r.bypass_suggestions))
    print("-" * 90)

# 📦 Export to Mistral-ready format
export_to_mistral_ready(results)
