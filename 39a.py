a,b=map(int,input().split())
#a
A=str(a)
B=str(b)
A_ans=0
B_ans=0
flag=False
flag_2=False

if A[0]!="9":
    A_ans+=900
    flag=True
else:
    A_ans+=int(A[0])*100


if A[1]!="9" and flag==False:
    A_ans+=90
    flag=True
else:
    A_ans+=int(A[1])*10

if A[2]!="9" and flag==False:
    A_ans+=9
    flag=True
else:
    A_ans+=int(A[2])


if B[0]!="1":
    B_ans+=100
    flag_2=True
else:
    B_ans+=int(B[0])*100


if B[1]!="0" and flag_2==False:
    B_ans+=0
    flag_2=True
else:
    B_ans+=int(B[1])*10


if B[2]!="0" and flag_2==False:
    B_ans+=0
    flag_2=True
else:
    B_ans+=int(B[2])


ans=max(a-B_ans,A_ans-b,a-b)
print(ans)