
import sys
input=sys.stdin.readline

.rstrip("\n")


=list(map(int,input().split()))

# 切り捨て
4 // 3
# 切り上げ
-(-4 // 3)

import sys

stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))



# 階乗
from math import factorial as fac

# combination
from itertools import combinations as cmb

# 重複を許す場合
from itertools import combinations_with_replacement as cmb

# 順列組み合わせ
from itertools import permutations as per
per(list,int)
# len(list) P int
per(list)
#len(list) P len(list) (intなしの場合)

# list.countを全要素に実施し、dictのラッパーCounterクラスで返す
# l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
# cnt(l)
# => Counter({'a': 4, 'c': 2, 'b': 1})
from collections import Counter as cnt



#再帰制限UP
import sys
sys.setrecursionlimit(2000000)


#最小公倍数 a is a list
from math import gcd
def lcm(a):
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // gcd(x, a[i])
    return x


#modの割り算　逆元　div(a,b) a/b mod mod
import sys
sys.setrecursionlimit(2000000)
mod = 1000000007

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def div(a, b):
    return mul(a, pow(b, mod-2,mod)) % mod


#累乗 二分累乗法　power(x,y) x**y
# 組み込み関数pow(x,y,mod)のほうが早い！！！！！
# def power(x, y):
#     if   y == 0     : return 1
#     elif y == 1     : return x % mod
#     elif y % 2 == 0 : return power(x, y/2)**2 % mod
#     else            : return power(x, y//2)**2 * x % mod


# コンビネーション cmb(n,r,mod) nCr mod mod
mod = 10**9+7 #出力の制限
n = 10**4 # nの最大値を指定
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル
for i in range( 2, n + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
def cmb(n, r):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


from functools import reduce
def comb(n, max_k, mod):
    """
    (n,k) := n個からk個選ぶ組み合わせ
    k = 0~max_Kまでを計算して返す
    """
    res = [1] * (max_k + 1)
    t = 1
    for i in range(max_k + 1):
        res[i] *= t
        t *= n - i
        t %= mod

    n = reduce(lambda x, y: (x * y) % mod, range(1, max_k + 1), 1)
    n = pow(n, -1, mod)

    for i in reversed(range(max_k + 1)):
        res[i] *= n
        res[i] %= mod
        n *= i
        n %= mod
    return res


#nが非常に大きくrがちいさいときはこっち
# 上にあるmul,divが必要
def cmb(n,r):
    res=1
    for i in range(1,r+1):
        res=res*div(n-i+1,i)%mod
    return res%mod


#queue
from collections import deque

L=deque([1,2,3,4])
#push,enqueue
L.append(5)#[1,2,3,4,5]
L.appendleft()
#pop
L.pop()#[1,2,3,4]
#dequeue
L.popleft()#[2,3,4]

# queueでスライスする
itertools.islice(iterable, stop)
itertools.islice(iterable, start, stop[, step])

#初期化を関数によって行うdict
# aaa = defaultdict(int|list|lambda ...)
from collections import defaultdict


# UnionFind
par=[i for i in range(n)]
# roはグループの大きさ
# ro=dict()
#
# for i in range(n):
#     ro[i]=1
i
def root(i):
    if par[i]==i:
        return i
    else:
        a=root(par[i])
        par[i]=a
        return a

def unite(x,y):
    rx=root(x)
    ry=root(y)
    if rx!=ry:
        par[rx]=ry
        # ro[ry]+=ro[rx]
        # ro[rx]=0


# 複数のgcd,lcm
import math
from functools import reduce
def gcd(numbers):
    return reduce(math.gcd, numbers)
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
def lcm(numbers):
    return reduce(lcm_base, numbers, 1)