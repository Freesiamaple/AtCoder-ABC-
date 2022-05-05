import math
P=int(input())
count=0
for i in range(1,11)[::-1]:
    if P<math.factorial(i):
        continue
    else:
        num=P//(math.factorial(i))
        count+=num
        P-=num*(math.factorial(i))
print(count)
