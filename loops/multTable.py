def multTable(n):
    mult = 0
    if n == 0:
        print("Please enter a number")
    else:
        for i in range(1, 11):
            mult = n * i
            print(mult)

print("Enter an integer: ")
n = int(input("> "))
multTable(n)

