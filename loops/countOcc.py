list = [10, 20, 10, 30, 10, 40, 50]
target = 40

count = 0


for i in list:
    if i == target:
        count += 1

print(f"{target} appears {count} times")        

