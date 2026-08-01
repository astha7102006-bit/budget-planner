import json
import os

FILE_NAME = "budget_data.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return {"budget": 0, "expenses": []}
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=2)

def set_budget(data):
    amount = float(input("Enter monthly budget: "))
    data["budget"] = amount
    save_data(data)
    print(f"Budget set to {amount}")

def add_expense(data):
    category = input("Category: ")
    amount = float(input("Amount: "))
    data["expenses"].append({"category": category, "amount": amount})
    save_data(data)

    total_spent = sum(e["amount"] for e in data["expenses"])
    remaining = data["budget"] - total_spent

    print(f"Added {category}: {amount}")
    if remaining < 0:
        print(f"Warning: You are over budget by {abs(remaining):.2f}!")
    else:
        print(f"Remaining budget: {remaining:.2f}")

def view_summary(data):
    if data["budget"] == 0:
        print("No budget set yet.")
        return

    total_spent = sum(e["amount"] for e in data["expenses"])
    remaining = data["budget"] - total_spent

    print(f"\nBudget: {data['budget']}")
    print(f"Total spent: {total_spent}")
    print(f"Remaining: {remaining:.2f}")

    if remaining < 0:
        print("Status: OVER BUDGET")
    else:
        print("Status: On track")

    print("\nExpenses by category:")
    categories = {}
    for e in data["expenses"]:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]
    for cat, amt in categories.items():
        print(f"- {cat}: {amt}")

data = load_data()

while True:
    print("\n1. Set budget  2. Add expense  3. View summary  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        set_budget(data)
    elif choice == "2":
        add_expense(data)
    elif choice == "3":
        view_summary(data)
    elif choice == "4":
        break