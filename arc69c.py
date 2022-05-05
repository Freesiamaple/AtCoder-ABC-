n,m=map(int,input().split())
count_s=n
count_c=m//2
if count_s>=count_c:
    print(count_c)
    exit()
else:
    count=count_s
    count_s=0
    count_c=m-n*2
    amari=count_c//4
    count+=amari
    print(count)