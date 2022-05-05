K=int(input())
a,b=map(int, input().split())
def base_10(num_n,n):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10
A=base_10(a,K)
B=base_10(b,K)
print(A*B)