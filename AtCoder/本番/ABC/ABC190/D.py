n=int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

s=make_divisors(2*n)

ans=0
for i in s:
    j=(2*n)//i
    a=(i - j + 1)
    b=(i + j - 1)
    if a%2==0 and b%2==0:
        ans+=1

print(ans)
