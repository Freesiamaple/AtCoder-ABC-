from collections import defaultdict
n=int(input())
A=list(map(int, input().split()))
Q=int(input())
K = [list(map(int, input().rstrip('\n').split())) for _ in range(Q)]

d = defaultdict(list)
for i in range(n):
    d[A[i]].append(i)




def is_ok(arg,x):
    # 条件を満たすかどうか？問題ごとに定義.True かFalseをうまく返すようにする
    if arg==x:
        return True
    else:
        return False

def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    https://twitter.com/meguru_comp/status/697008509376835584?s=20
    '''
    while (abs(ok - ng) > 10**(-8)):#ここで精度を調整できる。整数なら>1でok
        mid = (ok + ng) / 2#整数なら//
        if is_ok(mid):
            ok = mid
