n,q=map(int, input().split())
X=list(map(int, input().split()))
K = [list(map(int, input().rstrip('\n').split())) for _ in range(n-1)]
vk = [map(int, input().split()) for _ in range(q)]
v,k = [list(i) for i in zip(*vk)]
chs = [[] for v in range(n)]
def fre(x,y):#xは頂点番号,yはKの次みるとこ
    for i in range(y,n-1):
        if K[y][0]!=x:
            fre(x+1,y+1)
        else:
            p = P[v - 1]
            # 親 p の子頂点リストに頂点 v を挿入
            chs[p].append(v)
