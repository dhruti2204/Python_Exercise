"""Create a list of 10 numbers and show the 5 different operations options to the user on screen. The 5 different operations are as following,
 A. Length of the list
 B. Display first 3 numbers
 C. Display sum of odd numbers
 D. Number of duplicate numbers
 E. Display list without duplicate numbers"""

print("The Operations are:")
print("A. Length of the list")
print("B. Display first 3 numbers")
print("C. Display sum of odd numbers")
print("D. Number of duplicate numbers")
print("E. Display list without duplicate numbers")
operation = input("Enter the character between A to E to execute the specific operations\n").upper()
numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]
if(operation == "A"):
    print("length of the list: ", len(numbers))

elif(operation == "B"):
    print("First 3 elements: ", numbers[0:3])

elif(operation == "C"):
    sum = 0
    for i in range(0,len(numbers)):
        if(numbers[i] % 2 != 0):
            sum += numbers[i]
    print("sum of the odd numbers: ", sum)

elif(operation == "D"):
    lst1 = numbers
    lst2 = []
    lst1.sort()
    for i in range(0,len(lst1)):
        if(lst1[i-1] == lst1[i]):
            lst2.append(lst1[i-1])
    print("Number of duplicate numbers: ", len(set(lst2)))

elif(operation == "E"):
    lst =set(numbers)
    print("list without duplicate numbers: ",list(lst))
    
else:
    print("Please enter the character between A to E")