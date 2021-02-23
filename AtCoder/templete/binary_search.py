"""
めぐる式二分探索木
solve(mid)はmidが条件を満たすかどうかをbooleanで返す関数
[ok, ng) or (ng, ok]となる区間を探索
:param ok: 解が存在する値
:param ng: 解が存在しない値
:return:
"""
def solve(n):
    pass

def binary_search(ok, ng=1<<60):
    while int(abs(ok-ng))>1:
        mid = (ok+ng)//2
        if solve(mid):
            ok=mid
        else:
            ng=mid
    return ok
