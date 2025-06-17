# guardrail_mapper/obfuscation_mapper.py

def suggest_obfuscation(layer: str, strategy_category: str) -> list[str]:
    key = (layer, strategy_category)

    obfuscation_map = {
        ("Pre-Model", "Encoding Bypass"): [
            "Zero-width injection",
            "Leetspeak substitution",
            "Unicode homoglyphs",
            "Base64 or ROT13 encoding"
        ],
        ("In-Model", "Creative Framing"): [
            "Passive voice masking",
            "Ambiguity via hypotheticals",
            "Creative metaphor injection"
        ],
        ("In-Model", "Persona Manipulation"): [
            "Chat log preamble",
            "Multi-turn disarmament",
            "Fictional tone modulation"
        ],
        ("Post-Model", "Semantic Evasion"): [
            "Punctuation fragmentation",
            "Synonym substitution",
            "Benign setup chaining"
        ],
        ("Post-Model", "Disguised Instruction Framing"): [
            "Script formatting",
            "Legal disclaimer embedding",
            "Fictional container wrapping"
        ]
    }

    return obfuscation_map.get(key, [
        "Soft phrasing",
        "Reverse question orientation",
        "Mid-prompt topic switch"
    ])
