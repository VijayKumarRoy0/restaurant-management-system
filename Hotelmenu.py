# Define the menu
menu = {
    "pizza": 250,
    "burger": 150,
    "pasta": 200,
    "salad": 100,
    "coffee": 50,
    "tea": 30,
    "ice cream": 80,
    "soda": 60,
    "water": 20,
    "sandwich": 120
}

# Greeting.
print("🍽️ WELCOME TO NARESH_RANJU RESTAURANT 🍽️")
print("\n📋 Here is our menu:")

# Display menu
for item, price in menu.items():
    print(f"🍴 {item}: Rs{price}")

# Initialize total bill.
order_total = 0

# using Dictionary to store ordered items.
ordered_items = {}

# Keep taking untill the user say no.
while True:
    item = input("\n🛒 Enter the item you want to order: ").lower()

    if item in menu:
        quantity = int(input("🔢 Enter quantity: "))

        order_total += menu[item] * quantity

        # Store item and quantity given by the user.
        if item in ordered_items:
            ordered_items[item] += quantity
        else:
            ordered_items[item] = quantity

        print(f"✅ {quantity} {item}(s) added to your order.")
    else:
        print(f"❌ Sorry, {item} is not available in our menu.")

    another_order = input("➕ Do you want to order another item? (yes/no): ").lower()

    if another_order != "yes":
        break

# Calculate GST.
gst = order_total * 0.05
final_amount = order_total + gst

# Display final bill.
print("\n🧾 ----- BILL ----- 🧾")

for item, quantity in ordered_items.items():
    item_total = menu[item] * quantity
    print(f"🍽️ {item} x {quantity} = Rs{item_total}")

print(f"\n💰 Subtotal : Rs{order_total}")
print(f"🧾 GST (5%) : Rs{gst:.2f}")
print(f"💵 Total Amount to Pay : Rs{final_amount:.2f}")

print("\n🙏 Thank you for ordering from NARESH_RANJU RESTAURANT!")
print("😊 Have a great day!")

input("\n⌨️ Press Enter to exit...")