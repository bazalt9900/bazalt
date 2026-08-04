print("=== UNIVERSAL CONVERTER ===\n")
print("1. KM to Miles")
print("2. KG to Pounds")
print("3. Celsius to Fahrenheit")
print("4. USD to EUR (rate: 1 USD = 0.92 EUR)\n")

choice = input("Choose option (1-4): ")
value = float(input("Enter value: "))

if choice == "1":
    result = value * 0.621371
    print(f"{value} KM = {result} Miles")
elif choice == "2":
    result = value * 2.20462
    print(f"{value} KG = {result} Pounds")
elif choice == "3":
    result = (value * 9/5) + 32
    print(f"{value}°C = {result}°F")
elif choice == "4":
    result = value * 0.92
    print(f"{value} USD = {result} EUR")
else:
    print("Invalid option!")