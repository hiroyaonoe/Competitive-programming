import sys
sys.setrecursionlimit(2000000)
input=sys.stdin.readline


n,a,b=map(int,input().split())

mod = 10**9+7

power={}

def xpower(x, y):
    key=str(x) + " " + str(y)
    try:
        return power[key]
    except:
        pass
    if   y == 0     :
        power[key]=1
        return power[key]
    elif y == 1     :
        power[key]=x % mod
        return power[key]
    elif y % 2 == 0 :
        power[key]=xpower(x, y/2)**2 % mod
        return power[key]
    else            :
        power[key] =xpower(x, y//2)**2 * x % mod
        return power[key]



def mul(a, b):
    return ((a % mod) * (b % mod)) % mod
def div(a, b):
    return mul(a, xpower(b, mod-2)) % mod


# def cmb(n,r):
#     res=1
#     for i in range(1,r+1):
#         res=res*div(n-i+1,i)%mod
#     return res%mod


cnt=(xpower(2,n)-1)%mod


res=1
c=min(a,b)
d=max(a,b)
for i in range(1,d+1):
    res=res*div(n-i+1,i)%mod
    if i==c:
        cnt=(cnt-res)%mod
cnt=(cnt-res)%mod


# cnt-=cmb(n,a)+cmb(n,b)
print(cnt)