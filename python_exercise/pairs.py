def find_pairs(numbers, n):
    numbers=set(numbers)
    result = []  
    seen = [] 
    
    for num in numbers:
        complement = n - num  
        
        if complement in seen:
            result.append(sorted([num, complement]))
        seen.append(num)

    return result

numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
n = 12

pairs = find_pairs(numbers, n)
print(pairs)
