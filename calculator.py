# Shalom's Engineering Calculator v2
# Built by eboshalom before University 

print("=== Shalom's Calculator v2 ===")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")

if b != 0:
    print(f"Division: {a / b}")
    print(f"Remainder: {a % b}")
else:
    print("Cannot divide by zero")

# JAMB Checker - your own feature
print("\n--- JAMB Checker ---")
jamb = int(input("Enter your JAMB score: "))

if jamb >= 200:
    print(f"{jamb} - Good! You have a chance for LAUTECH Engineering")
else:
    print(f"{jamb} - Keep pushing, you need 200+")

print("\nBuilt by Shalom | github.com/eboshalom")