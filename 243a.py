V,A,B,C=map(int, input().split())
count=0
while V>=0:
    count+=1
    if count%3==1:
        V-=A
    if count%3==2:
        V-=B
    if count%3==0:
        V-=C

if count%3==1:
        print("F")
if count%3==2:
        print("M")
if count%3==0:
        print("T")