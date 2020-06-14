
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
def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y/2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod
def div(a, b):
    return mul(a, power(b, mod-2)) % mod


#累乗 二分累乗法　power(x,y) x**y
def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y/2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod


# コンビネーション cmb(n,r,mod) nCr mod mod
def cmb(n, r,mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
mod = 10**9+7 #出力の制限
N = 10**4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル
for i in range( 2, n + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

a = cmb(n,r,mod)

#nが非常に大きくrがちいさいときはこっち
# div
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


