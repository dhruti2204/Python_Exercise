
"""first program"""
def fib(n):
    if(n<=1):
        return n
    else:
        return(fib(n-1) + fib(n-2))
n=8
l = fib(n)
print(l)


"""second program"""
numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]

def recursive_sum(numbers):
   if not numbers:
       return 0
   else:
       return numbers[0] + recursive_sum(numbers[1:])

l= recursive_sum(numbers)
print(l)