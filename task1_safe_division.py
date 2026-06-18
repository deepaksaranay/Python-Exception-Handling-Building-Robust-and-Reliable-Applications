# Task 1: Safe Division Utility
try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator
except ValueError:
    print("Error: Please enter numeric values only.")
except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")
else:
    print("Result:", result)
finally:
    print("Operation Complete")
