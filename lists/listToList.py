def basicListOps(list):
    if len(list) < 3:
        print("The list cannot be less than three items")
    else:
        print("Third element: " + str(list[2]))
        print("Length of list: "  + str(len(list)) + " items long")
    

numbers = [10, 20]
basicListOps(numbers)

    
