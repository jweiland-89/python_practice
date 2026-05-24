import sys

def prod_sum(num1, num2):
    prod = 0
    sum_ = 0
    if num1 * num2 <= 1000:
        prod = num1 * num2
        print(f"The result is {prod}")
    else:
        sum_ = num1 + num2
        print(f"The result is {sum_}")

while True:
    try:
        while True:
            print("Enter your FIRST number...")
            int1 = int(input("> "))
            print("Enter your SECOND number...")
            int2 = int(input("> "))
            prod_sum(int1, int2)
    except KeyboardInterrupt:
        print()
        sys.exit()
    except ValueError:
        print("************************************")
        print("DATA VALUE ERROR: MUST BE AN INTEGER")
        print("************************************")
