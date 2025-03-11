"""Print the following patterns."""
"""
* *   * *
*       * 

*       *
* *   * * """
for i in range(5):
    space = 1+(2*min(i,4-i))
    star = abs(2-i)
    for j in range(star):
        print("*",end=" ")
    for k in range(space):
        print(" ",end=" ")
    for j in range(star):
        print("*",end=" ")
    print()

