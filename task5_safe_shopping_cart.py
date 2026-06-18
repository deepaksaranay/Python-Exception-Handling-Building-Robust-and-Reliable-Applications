# Task 5: Mini Program - Safe Shopping Cart

cart = []

while True:
    value = input("Enter price (or q to quit): ")

    if value.lower() == 'q':
        break

    try:
        price = float(value)

        if price < 0:
            raise ValueError("Negative price not allowed")

        cart.append(price)

    except ValueError as e:
        print("Error:", e)

print("Total items:", len(cart))
print("Total bill:", sum(cart))
