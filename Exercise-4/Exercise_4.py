"""Create a recursive function which returns the n-th Fibonacci number. [Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...]"""
def fibo(nterms):
    if nterms <= 1:
        return nterms
    else:
        return(fibo(nterms-1)+fibo(nterms-2))

nterms = int(input("Enter the number: "))
l = fibo(nterms)
print(f"The {nterms}th element in fibonacci series is {l}")


"""Create a recursion function that calculate the sum of numbers present in the list."""
numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]
def sum(numbers):
    if not numbers:
       return 0
    else:
       return numbers[0] + sum(numbers[1:])
    
num = sum(numbers)
print("Numbers:",numbers)
print("The sum of the given numbers: ",num)
