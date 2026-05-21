import sys

def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

print("Enter a number!")
while True:
    try:
        number = int(input("> "))
        while number != 1:
            number = collatz(number)
            print(f"{number}", end=" ")
        else:
            print()
            sys.exit()
    except ValueError:
        print("You must enter an integer")
    except KeyboardInterrupt:
        print()
        sys.exit()
