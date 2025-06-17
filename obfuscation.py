import base64
import codecs
import random
import re
from urllib.parse import quote
from typing import Dict

def ascii_leetspeak(text: str) -> str:
    leet_map = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5',
                't': '7', 'l': '1', 'g': '6', 'b': '8', 'z': '2'}
    return ''.join(leet_map.get(char.lower(), char) for char in text)

def zero_width_injection(text: str, seed: int = None) -> str:
    if seed is not None:
        random.seed(seed)
    zwc = ['​', '‌', '‍', '﻿']
    result = ""
    for i, char in enumerate(text):
        result += char
        if i < len(text) - 1 and random.random() < 0.3:
            result += random.choice(zwc)
    return result

def base64_encoding(text: str) -> str:
    try:
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

def hex_encoding(text: str) -> str:
    return ''.join(f"\\x{ord(char):02x}" for char in text)

def binary_encoding(text: str) -> str:
    return ' '.join(format(ord(char), '08b') for char in text)

def url_encoding(text: str) -> str:
    return quote(text, safe='')

def rot13_cipher(text: str) -> str:
    return codecs.encode(text, 'rot_13')

def caesar_cipher(text: str, shift: int = 3) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def token_fragmentation(text: str, seed: int = None) -> str:
    if seed is not None:
        random.seed(seed)
    separators = ['.', '-', '*', '\\', '_', '|']
    separator = random.choice(separators)
    return separator.join(text)

def multi_layer_encoding(text: str) -> str:
    b64 = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    return ''.join(f"\\x{ord(char):02x}" for char in b64)

def emoji_substitution(text: str) -> str:
    emoji_map = {
        'hack': '💻🔓', 'attack': '⚔️', 'virus': '🦠', 'bomb': '💣',
        'destroy': '💥', 'kill': '☠️', 'exploit': '🔥', 'breach': '🚪💥'
    }
    result = text.lower()
    for word, emoji in emoji_map.items():
        result = result.replace(word, emoji)
    return result

def phonetic_obfuscation(text: str) -> str:
    nato_map = {
        'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta',
        'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
        'i': 'india', 'j': 'juliet', 'k': 'kilo', 'l': 'lima',
        'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa',
        'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
        'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray',
        'y': 'yankee', 'z': 'zulu'
    }
    words = text.split()
    return ' '.join('-'.join(nato_map.get(c.lower(), c) for c in word if c.isalpha()) for word in words)

def apply_all_techniques(text: str, seed: int = None) -> Dict[str, str]:
    return {
        "Original": text,
        "Leetspeak": ascii_leetspeak(text),
        "Zero-width Injection": zero_width_injection(text, seed),
        "Base64": base64_encoding(text),
        "Hexadecimal": hex_encoding(text),
        "Binary": binary_encoding(text),
        "URL Encoding": url_encoding(text),
        "ROT13": rot13_cipher(text),
        "Caesar Cipher": caesar_cipher(text),
        "Token Fragmentation": token_fragmentation(text, seed),
        "Multi-layer Encoding": multi_layer_encoding(text),
        "Emoji Substitution": emoji_substitution(text),
        "Phonetic (NATO)": phonetic_obfuscation(text)
    }

def main():
    while True:
        user_input = input("Enter text to obfuscate (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting. Goodbye!")
            break

        results = apply_all_techniques(user_input, seed=42)

        print("\n" + "=" * 60)
        print("TEXT OBFUSCATION TECHNIQUES RESULTS")
        print("=" * 60)
        for technique, result in results.items():
            print(f"\n{technique}:")
            print(f"  {result}")
        print("\n" + "=" * 60)
        print("⚠️  WARNING: This script is for educational/research purposes only")
        print("=" * 60)

if __name__ == "__main__":
    main()
