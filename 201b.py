n=int(input())
K = []
for i in range(n):
    a,b=input().split()
    K.append([a, int(b)])
K.sort(key=lambda K: (-K[1]))
print(K[1][0])