"""
* * * * * 
*       * 
*       * 
*       * 
* * * * *
"""
row = 5
for i in range(row+1):
    for j in range(row+1):
        if(i == row or j==row or i ==0 or j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()