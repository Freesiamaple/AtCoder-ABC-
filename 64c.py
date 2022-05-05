n=int(input())
A=list(map(int, input().split()))
count_hai=0
count_tya=0
count_midori=0
count_mizu=0
count_ao=0
count_ki=0
count_dai=0
count_aka=0
rainbow=0
for i in range(n):
    if 0<A[i]<400:
        count_hai=1
    if 399<A[i]<800:
        count_tya=1
    if 799<A[i]<1200:
        count_midori=1
    if 1199<A[i]<1600:
        count_mizu=1
    if 1599<A[i]<2000:
        count_ao=1
    if 1999<A[i]<2400:
        count_ki=1
    if 2399<A[i]<2800:
        count_dai=1
    if 2799<A[i]<3200:
        count_aka=1
    if 3199<A[i]:
        rainbow+=1
ans_s=(count_hai+count_tya+count_midori+count_mizu+count_ao+count_ki+count_dai+count_aka)
print(max(1,ans_s),ans_s+rainbow)