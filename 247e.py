n,x,y=map(int, input().split())
A=list(map(int, input().split()))
count=0
import bisect
index_X = [n for n, v in enumerate(A) if v == x]
index_Y = [n for n, v in enumerate(A) if v == y]
index_Xp = [n for n, v in enumerate(A) if v > x]
index_Yp = [n for n, v in enumerate(A) if v < y]
print(index_Xp,index_Yp)