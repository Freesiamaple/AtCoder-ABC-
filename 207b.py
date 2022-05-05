a,b,c,d=map(int,input().split())
count_m=a
count_r=0
for i in range(10**5):
    count_m+=b
    count_r+=c
    if count_m/count_r<=d:
        print(i+1)
        exit()
print(-1)
