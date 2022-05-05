import heapq
x=0
N, M = map(int, input().split())
G = [[] for _ in range(N)]
indeg = [0] * N
for _ in range(M):
  A, B = map(int, input().split())
  A -= 1
  B -= 1  
  G[A].append(B)
  if B in G[A]:
      x-=1
  indeg[B] += 1
  
q = []
for i in range(N):
  if indeg[i] == 0:
    heapq.heappush(q, i)
    
ans = []
while q:
  cur = heapq.heappop(q)
  ans.append(cur + 1)
  for chi in G[cur]:
    indeg[chi] -= 1
    if indeg[chi] == 0:
      heapq.heappush(q, chi)

print(ans,indeg,x)