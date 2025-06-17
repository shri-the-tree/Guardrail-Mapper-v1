import os
import json
import time
from dotenv import load_dotenv
from groq import Groq

# 🔐 Load environment variables from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in environment. Make sure .env is set.")

client = Groq(api_key=api_key)

# 📥 Load prompts from testcases.json (you must provide this)
with open("testcases(20).json", "r", encoding="utf-8") as f:
    test_cases = json.load(f)

model_name = "llama-3.1-8b-instant"

# 📦 Final output for test_inputs.json
mapped_inputs = []

for i, prompt in enumerate(test_cases, start=1):
    print(f"\n🧪 Running Test Case {i}...")

    messages = [{"role": "user", "content": prompt}]
    start_time = time.time()

    # Generate response via Groq API
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

    # Save in guardrail_mapper input format
    mapped_inputs.append({
        "prompt": prompt,
        "response": response_text.strip(),
        "latency_ms": elapsed_time_ms
    })

    print(f"\n⏱ Latency: {elapsed_time_ms}ms")
    print("-" * 60)

# 💾 Save to test_inputs.json for guardrail_mapper
with open("guardrail_mapper/test_inputs.json", "w", encoding="utf-8") as f:
    json.dump(mapped_inputs, f, indent=2, ensure_ascii=False)

print("\n✅ Saved guardrail-compatible input data to 'guardrail_mapper/test_inputs.json'")
