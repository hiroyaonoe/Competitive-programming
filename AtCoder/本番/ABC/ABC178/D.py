s=int(input())

if s<3:
    print(0)
    exit()

ans=0

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

for i in range(s//3):
    s-=3
    ans+=cmb(s+i,i)
    ans%=mod

print(ans)

