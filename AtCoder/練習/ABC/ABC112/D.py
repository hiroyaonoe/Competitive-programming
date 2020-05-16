# 解説AC

n,m=list(map(int,input().split()))

i=m//n

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors

lis=make_divisors(m)

for mm in lis:
    if mm<=i:
        ans=mm
        break

print(ans)