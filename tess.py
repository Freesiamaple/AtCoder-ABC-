L=[20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
count=0
for i in range(17,-23,-2):
    print(L[i%20])
    count+=1
#print(count)