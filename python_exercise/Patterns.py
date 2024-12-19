""" 1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15 """


n=6
current_number = 1
for i in range(1,n):
    for j in range(1,i+1):
        print(current_number," ",end="")
        current_number += 1
    print()

print()

""" * * _ * *
    * _ _ _ *
    _ _ _ _ _
    * _ _ _ *
    * * _ * * """

row = 5
for i in range(row):
    for j in range(row):
        if(i != 2):
            if (i == 0 and j % 2 == 0) or (i == 1 and j == 0) or (i == 1 and j == 4) or (i == 2) or (i == 3 and j == 0) or (i == 3 and j == 4) or (i == 4 and j % 2 == 0) or (i==0 and j==1) or (i==0 or j==4) or (i==4 and j==1) or (i==4 and j==3):
                print("*", end=" ")
            else:
                print(" ", end = " ")
    
    print()

print()

""" _ _ * _ _
    _ * * * _
    * * * * *
    _ * * * _
    _ _ * _ _"""

row = 5
for i in range(row):
    for j in range(row):
        if (i == 0 and j == 2) or (i == 1 and (j == 1 or j == 2 or j == 3)) or (i == 2) or (i == 3 and (j == 1 or j == 2 or j == 3)) or (i == 4 and j == 2):
            print("*",end=" ")
        else:
            print(" ", end =" ")
    print()


print()

"""*
    * *
    * _ *
    * _ _ *
    * * * * * """

row = 5
for i in range(1,row+1):
    for j in range(1,row+1):
        if j == 1 or j==i or i==row:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()

""" * * * * *
    * _ _ _ *
    * _ _ _ *
    * _ _ _ *
    * * * * * """

row = 5
for i in range(row):
    for j in range(row):
        if(i == 0 or i == row - 1 or j==0 or j== row - 1 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


