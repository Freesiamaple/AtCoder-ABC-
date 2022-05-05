n=int(input())
L = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
time=0
w=[]
while n not in w:
    L[n-1]