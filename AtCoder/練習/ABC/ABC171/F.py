k = int(input())
s = input()

l = len(s)
mod = 10**9+7 #出力の制限

n = l+k
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
def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y/2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod

ans = 0
com = comb(n+k,k,mod)

for i in range(l,l+k+1):
    ans = (ans+cmb(n-1+k-i,k-i,mod)*pow(25,k-(l+k-i),mod)*pow(26,l+k-i,mod)) % mod

print(ans)