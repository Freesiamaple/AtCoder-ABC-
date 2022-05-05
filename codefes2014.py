A=input()
B=int(input())
q,mod=divmod(B,len(A))
print(A[mod-1])