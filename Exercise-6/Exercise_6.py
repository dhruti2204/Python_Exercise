"""Find how many number of times the substring occurs in the given string."""
string = "PQRQRQRQ"
substring = "QRQ"

count = 0
x = len(string);y=len(substring)
for i in range(0,x):
    if(string[i:i+y] == substring):
        count+=1
print(count)