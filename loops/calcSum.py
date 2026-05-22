def sumAvg(number):
    accum = 0
    for i in range(1, number + 1):
        accum += i
    else:
        print(f"Sum is: {accum}")

print("Please enter a number")
number = int(input("> "))

sumAvg(number)
