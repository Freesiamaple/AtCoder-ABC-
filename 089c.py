n=int(input())
count_m=0
count_a=0
count_r=0
count_c=0
count_h=0
for i in range(n):
    S=(input())[0]
    if S=="M":
        count_m+=1
    if S=="A":
        count_a+=1
    if S=="R":
        count_r+=1
    if S=="C":
        count_c+=1
    if S=="H":
        count_h+=1
C=[count_m,count_a,count_r,count_c,count_h]
while 0 in C:
    C.remove(0)
if len(C)<3:
    print(0)
    exit()
ans=0
from itertools import *
B=list(combinations(C, 3))
for j in range(len(B)):
    ans+=B[j][0]*B[j][1]*B[j][2]
print(ans)
