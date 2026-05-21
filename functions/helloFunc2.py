def say_hello_to(name):
    # Prints three greetings to the name provided
    print("Good morning, " + name)
    print("Good afternoon, " + name)
    print("Good evening, " + name)

print("What's your name?")
nameInput = input("> ")

name = str(nameInput)

say_hello_to(name)
