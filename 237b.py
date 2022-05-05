h,w=map(int, input().split())
K = [list(map(int, input().rstrip('\n').split())) for _ in range(h)]
for x in zip(*K):
    print(*list(x))