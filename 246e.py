n=int(input())
a,b=map(int, input().split())
A=list(map(int, input().split()))

a,b=input().split()#文字列、数字

B = [int(input()) for i in range(5)] #縦に並んでるやつ

ab = [map(int, input().split()) for _ in range(m)]
a, b = [list(i) for i in zip(*ab)]
K = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]

x=[i for i in input()]

DP=[[0]*(n*M+1) for _ in range(n+1)]