rows = int(input("Enter number of rows: "))

print("Right Triangle Pattern")

for i in range(1, rows + 1):
    pattern = ""

    for j in range(i):
        pattern += "* "

    print(pattern)
