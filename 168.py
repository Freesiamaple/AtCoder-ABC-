import math
a,b,h,m=map(int,input().split())
sita_a=(h%12/12*math.pi*2)+m%60/60/12*math.pi*2
sita_b=(m%60/60*math.pi*2)
delta=min(abs(sita_a-sita_b),2*math.pi-abs(sita_a-sita_b))
ans_2=a**2+b**2-2*a*b*math.cos(delta)
print(math.sqrt(ans_2))