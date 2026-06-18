# Task 2: Bill Calculator with Error Handling
prices = [120, 350, 'abc', 500, -200, 800]
total = 0

for price in prices:
    try:
        if not isinstance(price, (int, float)):
            raise TypeError("Value is not a number")
        if price < 0:
            raise ValueError("Negative price not allowed")

        total += price
        print("Running Total:", total)

    except TypeError as e:
        print("TypeError:", e)
    except ValueError as e:
        print("ValueError:", e)
