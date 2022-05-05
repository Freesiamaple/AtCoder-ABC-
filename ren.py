n,k=map(int,input().split())
A=list(map(int, input().split()))
def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    return arg<=k


def meguru_bisect(ng, ok):

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok 
print(meguru_bisect(A[n-1],A[0]))