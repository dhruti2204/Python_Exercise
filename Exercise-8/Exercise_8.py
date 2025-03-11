"""You are given a list of numbers and your task is to sort the list without any inbuilt method of python."""
numbers = [2, 5, 6, 1, 3, 8, 9, 10]
for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if(numbers[i]>numbers[j]):
            numbers[i],numbers[j] = numbers[j],numbers[i]
print(numbers)
