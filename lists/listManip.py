testList = [100, 50, 400, 500]

print("Initial List Values: " + str(testList))

testList[1] = 200

print("Values after change: " + str(testList))

testList.append(600)

print ("Values after append: " + str(testList))

testList.insert(2, 300)

print("Values after insert :" + str(testList))

testList.remove(600)

print("Values after remove: " + str(testList))

testList.pop(0)

print("Values after pop: " + str(testList))
