#  Bakery Ingredient Manager

ingredients = {}

print(" Welcome to the Bakery Ingredient Manager! ")

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Add new ingredient")
    print("2. View all ingredients")
    print("3. Update ingredient quantity")
    print("4. Search for an ingredient")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1–5): ").strip()

    if choice == '1':
        name = input("Enter the name of the new ingredient: ").capitalize()
        if name in ingredients:
            print("⚠️ Ingredient already exists.")
            continue
        quantity = input(f"Enter quantity and unit (e.g., '10 kilos', '5 litres'): ").strip()
        ingredients[name] = quantity
        print(f"✅ {name} added with quantity: {quantity}")

    elif choice == '2':
        if not ingredients:
            print("📭 No ingredients added yet.")
        else:
            print("\n📋 Ingredient Stock:")
            for item, qty in ingredients.items():
                print(f"- {item}: {qty}")

    elif choice == '3':
        name = input("Enter the name of the ingredient to update: ").capitalize()
        if name not in ingredients:
            print("❌ Ingredient not found.")
            continue
        quantity = input(f"Enter new quantity and unit for {name}: ").strip()
        ingredients[name] = quantity
        print(f"🔄 {name} updated to: {quantity}")

    elif choice == '4':
        name = input("Enter the ingredient name to search: ").capitalize()
        if name in ingredients:
            print(f"🔎 {name}: {ingredients[name]}")
        else:
            print("❌ Ingredient not found.")

    elif choice == '5':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

