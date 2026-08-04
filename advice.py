"""
===========================================
RANDOM ADVICE GENERATOR
===========================================
Gives you a random life advice every time you run it.
Just run: python advice.py

Example output:
=== YOUR RANDOM ADVICE ===
Pet your cat
Follow it wisely!
===========================================
"""

import random

advice_list = [
    "Pet your cat",
    "Drink a glass of water",
    "Restart your router",
    "Say something nice to someone",
    "Do nothing for 5 minutes",
    "Go outside and breathe",
    "Listen to your favorite song",
    "Smile at yourself in the mirror"
]

print("=== YOUR RANDOM ADVICE ===\n")
print(random.choice(advice_list))
print("\nFollow it wisely!")