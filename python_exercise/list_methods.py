print("Select the option")
print("A : length of the list")
print("B : Display first 3 numbers")
print("C : Display sum of odd numbers")
print("D : Number of duplicate numbers")
print("E : Display list without duplicate numbers")
i = input("Enter the charachter between A to E to show the required operation which is mentoined above\n")
numbers= [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]
if i=="A" or i=='a':
    print("length of the list is:",len(numbers))
elif i=="B" or i=='b':
    l1=[]
    for j in range(3):
        l1.append(numbers[j])
    print("First 3 number:",l1)
elif i=="C" or i=="c":
    sum=0
    for k in range(0,len(numbers)):
        if numbers[k] % 2!=0:
            sum=sum + numbers[k]
    print("Sum of odd numbers:",sum)
elif i=="D" or i=="d":
    seen = set()  
    duplicates = set()  
    for num in numbers:
        if num in seen:
            duplicates.add(num)  
        else:
            seen.add(num)         
    print("Number of duplicates numbers:",len(duplicates))
elif i=="E" or i=="e":
    l3=set(numbers)
    print("List without duplicate numbers:", list(l3))
else:
    print("Enter the valid option")

