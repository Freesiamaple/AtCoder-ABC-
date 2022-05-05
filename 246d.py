n=int(input())

def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    if (a**2+arg**2)*(a+arg)>=n:
        return True
    return False



def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    https://twitter.com/meguru_comp/status/697008509376835584?s=20
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok 

ans=set()

for a in range(2*10**6):
    b=meguru_bisect(-1,10**6+1)
    ans.add((a**2+b**2)*(a+b))
print(min(ans))
