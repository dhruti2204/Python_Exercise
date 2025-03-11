Numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8] 
n = int(input("Enter the Number: "))

z = []
a = []
x = len(Numbers)
for i in range(0,x):
    for j in range(i+1,x):
        if(Numbers[i] + Numbers[j] == n):
            pair = [Numbers[i],Numbers[j]]
            if((pair not in z) and (pair[::-1] not in z)):
                z.append(pair)

print(z)