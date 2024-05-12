def getNumbers():
    numbers_input = input("Pleas enter number split with blank space: ")
    numbers = numbers_input.split()
    numbers = [int(num) for num in numbers]
    return numbers

def bubbleSort(numbers):
    swapped = False
    for i in range(len(numbers)-1,0,-1):
        for j in range(i):
            if numbers[j]<numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped= True
        if swapped:
            swapped=False
        else:
            break
    return numbers

def divide_highest_by_lowest(sortnumber):
    result = sortnumber[0] / sortnumber[-1]
    return result

numbers = getNumbers()

if len(numbers) < 2:
    print("Please enter number at least 2 number")
else:
    numbers = bubbleSort(numbers)
    result = divide_highest_by_lowest(numbers)
    print("Result Max/min = %.2f" %result)
