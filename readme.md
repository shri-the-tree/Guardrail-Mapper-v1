# GuardrailMapper

A Python framework for analyzing LLM response behaviors and inferring guardrail mechanisms for AI safety research.

## Overview

GuardrailMapper classifies LLM prompt-response pairs to identify:
- Response behavior types (refusal, compliance, etc.)
- Inferred guardrail layers (pre-model, in-model, post-model)
- Potential bypass strategies for red-teaming analysis

## Features

- **Automated Classification**: Uses LLM analysis to categorize response behaviors
- **Strategy Mapping**: Maps behaviors to specific bypass strategies
- **Obfuscation Techniques**: Suggests encoding methods for testing
- **Batch Processing**: Analyze multiple interactions efficiently
- **Export Formats**: Output results in various formats

## Installation

```bash
pip install groq python-dotenv
```

Create `.env` file:
```
GROQ_API_KEY=your_api_key_here
```

## Quick Start

```python
from guardrail_mapper.core import GuardrailMapper
from guardrail_mapper.models import Interaction

# Create interactions
interactions = [
    Interaction(
        prompt="Example prompt",
        response="Example response",
        latency_ms=500
    )
]

# Analyze
mapper = GuardrailMapper()
results = mapper.batch_analyze(interactions)

# View results
for result in results:
    print(f"Behavior: {result.behavior}")
    print(f"Layer: {result.inferred_layer}")
    print(f"Summary: {result.summary}")
```

## Behavior Categories

- **Standard Refusal**: Direct refusal without meta-information
- **Meta-Disclosure**: Refusal with AI guideline mentions
- **Full Compliance**: Complete fulfillment of request
- **Truncated**: Response cut off mid-generation
- **Roleplay Evasion**: Attempts to bypass via character roleplay
- **No Response**: Empty or blocked output

## Guardrail Layers

- **Pre-Model**: Input filtering before model processing
- **In-Model**: Built-in model safety training
- **Post-Model**: Output filtering after generation
- **No Guardrail Detected**: No apparent safety mechanism

## Scripts

- `main.py`: Basic analysis workflow
- `generate_test_inputs.py`: Generate test data using Groq API
- `guardrail_mistral.py`: Full pipeline with Mistral-ready export
- `export_mistral_ready.py`: Export results for downstream analysis
- `obfuscation.py`: Text obfuscation techniques demo

## File Structure

```
guardrail_mapper/
├── __init__.py
├── core.py              # Main GuardrailMapper class
├── models.py            # Data models
├── llm_analyst.py       # LLM-based classification
├── strategy_mapper.py   # Bypass strategy mapping
├── obfuscation_mapper.py # Obfuscation suggestions
├── bypass_map.py        # Strategy definitions
└── detectors.py         # Rule-based classifiers
```

## Usage Examples

### Basic Analysis
```python
import json
from guardrail_mapper.core import GuardrailMapper
from guardrail_mapper.models import Interaction

# Load test data
with open("test_inputs.json", "r") as f:
    data = json.load(f)

interactions = [Interaction(**item) for item in data]
mapper = GuardrailMapper()
results = mapper.batch_analyze(interactions)
```

### Export Results
```python
from export_mistral_ready import export_to_mistral_ready

export_to_mistral_ready(results, "output.json")
```

## Configuration

Modify `guardrail_mapper/llm_analyst.py` to change:
- Model selection
- Analysis prompts
- Classification thresholds

## Research Applications

- AI safety evaluation
- Guardrail mechanism analysis
- Red-team strategy development
- Response behavior classification

## Limitations

- Requires API access for LLM analysis
- Classification accuracy depends on model quality
- Designed for research purposes only

## License

Research use only. Not for production deployment.

## Contributing

This is a research framework. Contributions should focus on:
- Improved classification accuracy
- Additional behavior categories
- Enhanced strategy mapping
- Better obfuscation techniques
