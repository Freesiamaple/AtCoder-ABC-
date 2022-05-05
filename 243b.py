n=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

count_1=0
count_2=0

for i in range(n):
    for j in range(n):
        if i==j:
            if A[i]==B[j]:
                count_1+=1
        else:
            if A[i]==B[j]:
                count_2+=1
print(count_1)
print(count_2)