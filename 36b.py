n=int(input())
A = [str(input()) for i in range(n)]
for x in zip(*A):
    print(''.join(x)[::-1])