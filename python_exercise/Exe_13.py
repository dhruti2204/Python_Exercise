from functools import reduce

class Number:
    def __init__(self, numbers):
        self.numbers = numbers

    def get(self):
        return self.numbers
    
    def change_original_values(self, func: lambda x: x): # func has default value
        # Use python map() here
        new_numbers =  list(map(func, self.numbers)) #your code, apply passed function here map
        return new_numbers
    
    def filter_values(self, filter_func: lambda x: x):
        # Use python filter() here
        filtered_numbers = list(filter(filter_func,self.numbers)) # Your code, apply passed function here
        return filtered_numbers
    
    def compound_the_numbers(self, reduce_func: lambda compound, d: compound + d):
        # Use python reduce() here: terminal function that returns single value compounded by reduce_func
        compounded_value = reduce(reduce_func, self.numbers)
        return compounded_value
    
    def sort(self):
        # Sort the list and return sorted list
        return sorted(self.numbers)
    
if __name__ == "__main__":
    numbers = [2, 5, 1, 66, 22, 11, 10]
# Create an object of Number class and initialize it.
n1 = Number(numbers)

# Print the list
print("Numbers: ", n1.get())

lambda_func1 = lambda x : x * 2 
print("New values:", n1.change_original_values(func=lambda_func1))

lambda_func2 = lambda x: x % 2 == 0 
print("Filtered values:", n1.filter_values(filter_func=lambda_func2))

lambda_func3 = lambda compound, d: compound + d
print("Compounded value:", n1.compound_the_numbers(reduce_func=lambda_func3))

# Sort the list
print("Sorted list:", n1.sort())



