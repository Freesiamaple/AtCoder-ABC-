a,n=map(int, input().split())
from collections import deque


import sys
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限
def dfs(x,y):
    if len(str(x))>n:
        
        return

    dfs(x*a,y)
    d=deque(str(x))
    d.rotate()
    x=int(str(d))
    dfs(x,y)

