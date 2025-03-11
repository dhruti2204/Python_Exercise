"""
    *    
  * * * 
* * * * * 
  * * *  
    *
"""
for i in range(5):
    star = 1+(2*min(i,4-i))
    space = abs(2-i)
    for j in range(space):
        print(" ",end=" ")
    for k in range(star):
        print("*",end=" ")
    for j in range(space):
        print(" ",end=" ")  
    print()