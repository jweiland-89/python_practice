def cube_int(n):
    exp = 0
    if n == 0:
        print("Number must be greater than 0...")
    else:
        for i in range (1, n + 1):
            exp = i ** 3
            print(f"Current Number is : {i} and the cube is {exp}")

print("Enter a number (must be greater than 0)")
nInput = int(input("> "))
cube_int(nInput)
