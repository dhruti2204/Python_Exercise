""" Here you are given two series input one is arithmetic progression (A.P.) and another one is geometric progress (G.P.).
 In which, one of the terms is wrong. Your task is to find out the wrong term and replace it with correct term."""


AP = [2, 5, 8, 11, 15, 17]
difference = AP[1] - AP[0]

for i in range(2,len(AP)):
    if((AP[i]-AP[i-1]) != difference):
        AP[i]= AP[i-1]+difference
           
print(AP)

GP = [3, 6, 9, 12, 16, 18]
ratio = int(GP[1]/GP[0])
for i in range(2,len(GP)):
    if((GP[i]/GP[i-1])!=ratio):
        GP[i]=GP[i-1]*ratio

print(GP)


