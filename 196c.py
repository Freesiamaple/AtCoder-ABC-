n=input()
mL=len(n)
if mL==1:
    print(0)
    exit()
flag=1
if mL%2!=0:
    mL-=1
    flag-=1
#mL means max len,flag means n is 9…9 if flag==0
num_r=str(9999999)
if flag==0:
    num="9"*(mL//2)
else:
    s = [str(c) for c in n]
    num=str()
    num_r=str()
    for k in range(mL//2):
        num+=s[k]
        num_r+=s[k+mL//2]
#think under num
if num>num_r:
    print(int(num)-1)
else:
    print(num)