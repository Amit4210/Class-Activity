from model import TipModel

# Initializing with $50, 20% tip, and 2 people
tip_model = TipModel(50.00, 20, 2)

print(f"--- Initial State ---")
print(f"Bill: ${tip_model.bill_amount}")
print(f"Tip %: {tip_model.tip_percent * 100}%")
print(f"Number of people: {tip_model.num_people}")
print(f"Total per person: ${tip_model.total_per_person:.2f}")
print(f"String representation: {tip_model}")

# Testing updates to the new attributes
print(f"\n--- Testing Updates ---")
tip_model.bill_amount = 100.00
tip_model.tip_percent = 15
tip_model.num_people = 5
print(f"New Total per person: ${tip_model.total_per_person:.2f}")

# Testing Validation (The "Call-out" Section)
print(f"\n--- Testing Logic Errors ---")

try:
    print("Attempting to set people to 0...")
    tip_model.num_people = 0
except ValueError as ex:
    print(f"Caught expected error: {ex}")

try:
    print("Attempting to set negative bill...")
    tip_model.bill_amount = -10.00
except ValueError as ex:
    print(f"Caught expected error: {ex}")

print(f"\nFinal State Check: {tip_model}")
