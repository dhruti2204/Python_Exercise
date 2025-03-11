"""
* 
* *
*   *
*     * 
* * * * *
"""
row = 5
for i in range(1,row+1):
    for j in range(1,row+1):
        if j == 1 or j==i or i==row:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
