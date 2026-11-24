number = int(input("Enter a number: "))

print("Multiplication Table")
print("--------------------")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

def calculate_square(n):
    return n * n
