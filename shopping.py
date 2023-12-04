total_price = 0
total_items = 0
total_pounds = 0

def Dry_Cured_Iberian_Ham(user_input_pounds):
    price_per_pound = 177.80
    total_price = price_per_pound * user_input_pounds
    return total_price, user_input_pounds

def Wagyu_steaks(user_input_pounds):
    price_per_pound = 450.00
    total_price = price_per_pound * user_input_pounds
    return total_price, user_input_pounds

def Matsutake_Mushroom(user_input_pounds):
    price_per_pound = 272.00
    total_price = price_per_pound * user_input_pounds
    return total_price, user_input_pounds

def Kopi_Luwak(user_input_pounds):
    price_per_pound = 306.50
    total_price = price_per_pound * user_input_pounds
    return total_price, user_input_pounds

def Moose_Cheese(user_input_pounds):
    price_per_pound = 487.20
    total_price = price_per_pound * user_input_pounds
    return total_price, user_input_pounds

def White_truffle(user_input_pounds):
    price_per_pound = 3600.00
    total_price = price_per_pound * user_input_pounds
    return total_price, user_input_pounds

def Blue_fin_tuna(user_input_pounds):
    price_per_pound = 3603.00
    total_price = price_per_pound * user_input_pounds
    return total_price, user_input_pounds

def Le_Bonnotte_potatoes(user_input_pounds):
    price_per_pound = 270.81
    total_price = price_per_pound * user_input_pounds
    return total_price, user_input_pounds

food_items = [
    "Dry cured Iberian ham",
    "Wagyu steak",
    "Matsutake mushroom",
    "Kopi Luwak coffee",
    "Moose cheese",
    "White truffle",
    "Blue fin tuna",
    "Le Bonnotte potatoes"
]

print("Welcome to Alvin Ganteng supermarket")
print("Food Item ")

for i, item in enumerate(food_items, start=1):
    print(f"{i}. {item}")

def order_items():
    amount_items = int(input("How many items you order today? : "))
    while amount_items < 1:
        print("Number of items must be at least 1")
        amount_items = int(input("How many items you order today? : "))

    items = []

    for i in range(1, amount_items + 1):
        while True:
            print(f"Item #{i} - ")
            item_number = int(input("Enter item number : "))
            if 1 <= item_number <= len(food_items):
                food = food_items[item_number - 1]
                break
            else:
                print("Warning: Invalid item number. Please enter a valid item number.")

        pounds = float(input("Enter amount of pounds: "))
        while pounds <= 0:
            print("Amount of pounds must be greater than 0.")
            pounds = float(input("Enter amount of pounds: "))

        item = {"food": food, "pounds": pounds}
        items.append(item)

    return items

ordered_items = order_items()
print("Ordered Items:")
for i, item in enumerate(ordered_items, start=1):
    food_type = item['food'].replace(" ", "_").lower()
    total, pounds = globals()[food_type](item['pounds'])
    total_price += total
    total_items += 1
    total_pounds += pounds
    print(f"Item #{i}: {item['food']} - {item['pounds']} pounds - Total Price: ${total:.2f}")

print(f"Total Items: {total_items}, Total Pounds: {total_pounds:.2f}, Grand Total Price: ${total_price:.2f}")
