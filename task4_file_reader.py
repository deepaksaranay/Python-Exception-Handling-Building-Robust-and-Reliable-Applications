# Task 4: File Reader with Exception Handling

filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        for i in range(3):
            line = file.readline()
            if not line:
                break
            print(line.strip())

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File operation attempted.")
