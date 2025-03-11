from functools import reduce

class Number:
    def __init__(self, numbers):
        self.numbers = numbers

    def get(self):
        return self.numbers 
    
    def change_original_values(self, func): 
        new_numbers =  list(map(func, self.numbers)) 
        return new_numbers
    
    def filter_values(self, filter_func):
        filtered_numbers = list(filter(filter_func,self.numbers)) 
        return filtered_numbers 
    
    def compound_the_numbers(self, reduce_func): 
        compounded_value = reduce(reduce_func, self.numbers)
        return compounded_value
        
    def sort(self):
        return sorted(self.numbers)
            
if __name__ == "__main__": 
    numbers = [2, 5, 1, 66, 22, 11, 10]
            
    n1 = Number(numbers)
    print("Numbers: ", n1.get())
            
    print("New values:", n1.change_original_values(func=lambda x : x * 2))
    print("Filtered values:", n1.filter_values(filter_func=lambda x : x % 2 == 0 ))
    print("Compounded value:", n1.compound_the_numbers(reduce_func=lambda x,y : x+y))
    print("Sorted list:", n1.sort())