import math
N=int(input())
n=math.floor((2*N)**(1/2))+1
sa=n*(n+1)/2-N
if sa==0:
    for i in range(n):
        print(i+1)
    exit()
for i in range(n):
    if i+1==sa:
        continue
    else:
        print(i+1)