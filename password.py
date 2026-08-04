import random

adjectives = ["Crazy", "Sleepy", "Loud", "Shy", "Bold", "Wild", "Cool"]
nouns = ["Cat", "Dragon", "Pizza", "Ninja", "Panda", "Tiger", "Robot"]
numbers = random.randint(10, 99)
symbols = ["!", "@", "#", "$", "%"]

adj = random.choice(adjectives)
noun = random.choice(nouns)
symbol = random.choice(symbols)

password = adj + noun + str(numbers) + symbol

print("=== FUNNY PASSWORD GENERATOR ===\n")
print(f"Your password: {password}")
print("\nEasy to remember, hard to crack!")