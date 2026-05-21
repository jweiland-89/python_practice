import sys

while True:
    print("Type exit to exit. ")
    response = input(">")
    response = response.lower() 
    if response == "exit":
        sys.exit()
    print("You typed " + response + ".")
