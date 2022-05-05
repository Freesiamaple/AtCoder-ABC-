import math
n=int(input())
if n==0:
    print("Yes")
    exit()

x=math.log(abs(n),2)

if -31<=x<31:
    print("Yes")
    exit()
if x==31 and n<0:
    print("Yes")
    exit()
if n==-2147483648:
    print("Yes")
    exit()
print("No")