testList = [10, 20, 30, 40, 50]

def sumAvg(list):
    listSum = sum(list)
    print(f"Sum: {listSum}")
    avg = listSum // len(list)
    print(f"Average: {avg}")

sumAvg(testList)
