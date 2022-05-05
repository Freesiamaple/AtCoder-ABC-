n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
time=0
people=n
if n%a==0:
    time+=n//a
else:
    time+=n//a+1
    people=n-n//a

if people%b==0:
    time+=people//b
else:
    time+=people//b+1
    people=people%b

if people%c==0:
    time+=people//c
else:
    time+=people//c+1
    people=people%c

if people%d==0:
    time+=people//d
else:
    time+=people%d+1
    people=people%d

if people%e==0:
    time+=people//e
else:
    time+=people//e+1
    people=people%e
print(time)