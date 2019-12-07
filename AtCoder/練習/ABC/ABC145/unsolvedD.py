from math import factorial as fac
mod=10**9+7
x,y=map(int,input().split())
if (x+y)%3==0:
    n=y-(x+y)/3
    m=x-(x+y)/3
    if (n>=0)&(m>=0):
        ans=fac(n+m)/(fac(n)*fac(m))
    else:ans=0
else:ans=0
print(int(ans%mod))

#MODの計算でTLE
#逆元云々でMOD計算は高速化できるらしい
#蟻本参照