# Bakery Stock Management Program

# Initial stock quantities
stock = {
    "Bread": 50,
    "Croissant": 30,
    "Cake": 20,
    "Muffin": 25,
    "Eclair": 15
}

# Start program
print("🍞 Welcome to the Bakery Stock Manager! 🍰")

while True:
    print("\n--- Current Stock ---")
    for item, quantity in stock.items():
        print(f"{item}: {quantity} units")

    action = input("\nType 'in' to add stock, 'out' to remove stock, or 'done' to finish: ").lower()

    if action == 'done':
        print("\n📦 Final Stock Report:")
        for item, quantity in stock.items():
            print(f"{item}: {quantity} units")
        print("✅ Stock update completed. Thank you!")
        break

    if action not in ['in', 'out']:
        print("⚠️ Invalid action. Please enter 'in', 'out', or 'done'.")
        continue

    product = input("Enter product name: ").capitalize()

    if product not in stock:
        print("❌ This product is not in the stock list.")
        continue

    try:
        amount = int(input(f"How many units to {'add' if action == 'in' else 'remove'}? "))
        if amount < 0:
            print("⚠️ Quantity must be a positive number.")
            continue
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    if action == 'in':
        stock[product] += amount
        print(f"✅ {amount} {product}(s) added. New stock: {stock[product]}")
    elif action == 'out':
        if amount > stock[product]:
            print(f"⚠️ Not enough {product} in stock to remove {amount}.")
        else:
            stock[product] -= amount
            print(f"✅ {amount} {product}(s) removed. New stock: {stock[product]}")

