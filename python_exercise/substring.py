def substring(string, sub):
    count=0
    for i in range(0,len(string)):
        a=string[i:i+3]
        if(a==sub):
            count+=1
    return count

string = "PQRQRQRQ"
sub = "QRQ"
num = substring(string,sub)
print(num)