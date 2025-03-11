"""You are given a list of person names. Your task is to find out the three most frequent and three least frequent names."""

names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']
lst = []
print("Names:", names)
for i in range(0,len(names)):
    lst.append(len(names[i]))
print("Name lengths: ",lst)

length_count = {}
for length in lst:
    if length in length_count:
        length_count[length] += 1
    else:
        length_count[length] = 1
sort_length = sorted(length_count.items(), key = lambda x: x[1], reverse = True)

most_frequent =  sort_length[:3]
least_frequent = sort_length[-3:]

print("\nThe three most frequent name lengths are:")
for length, count in most_frequent:
    names_with_length = [names[i] for i in range(len(names)) if len(names[i]) == length]
    print(f"{count} names of length {length}: {names_with_length}")
    
print("\nThe three least frequent name lengths are:")
for length, count in least_frequent:
    names_with_length = [names[i] for i in range(len(names)) if len(names[i]) == length]
    print(f"{count} names of length {length}: {names_with_length}")