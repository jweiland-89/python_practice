givenString = "Loops are fun!"

vowels = "aeiou"

vowelCount = 0

consCount = 0

for i in givenString.lower():
    if i.isalpha():
        if i in vowels:
            vowelCount += 1
        else:
            consCount += 1



print(f"Vowels: {vowelCount}")
print(f"Consonants: {consCount}")
