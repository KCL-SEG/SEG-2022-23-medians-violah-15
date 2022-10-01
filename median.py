"""Median calculator."""
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
#sort the list
numbers.sort()
#find the median number
if len(numbers)%2 == 0:
    sum = numbers[int(len(numbers)/2)] + numbers[int(len(numbers)/2 -1)]
    median = sum/2
    print(f'Median of list is: {median}')
else:
    median = numbers[int((len(numbers)-1)/2)]
    print(f'Median of list is: {median}')
