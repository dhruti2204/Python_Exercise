"""
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
row = 5
current_num = 1
for i in range(row):
    for j in range(i+1):
        print(current_num,end=" ")
        current_num +=1
    print()