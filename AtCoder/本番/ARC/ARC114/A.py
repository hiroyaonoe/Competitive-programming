import math
from collections import defaultdict

n = int(input())
x = list(map(int, input().split()))

# num以下の素数列挙(math必要)
def make_prime_list(num):
    if num < 2:
        return []

    # 0のものは素数じゃないとする
    prime_list = [i for i in range(num + 1)]
    prime_list[1] = 0 # 1は素数ではない
    num_sqrt = math.sqrt(num)

    for prime in prime_list:
        if prime == 0:
            continue
        if prime > num_sqrt:
            break

        for non_prime in range(2 * prime, num, prime):
            prime_list[non_prime] = 0

    return [prime for prime in prime_list if prime != 0]

prime_list = make_prime_list(max(x))
# 素因数分解(make_prime_list,mathが必要)
# key:素因数 value:個数
def prime_factorization(num):
    if num <= 1:
        return False
    else:
        dict_counter = {}
        for prime in prime_list:
            while num % prime == 0:
                if prime in dict_counter:
                    dict_counter[prime] += 1
                else:
                    dict_counter[prime] = 1
                num //= prime
        if num != 1:
            if num in dict_counter:
                dict_counter[num] += 1
            else:
                dict_counter[num] = 1

        return dict_counter

primes = defaultdict(list)
for i in range(n):
    p = prime_factorization(x[i])
    for k in p.keys():
        primes[k].append(i)

l = len(primes)
ans=[]
for i in range(1 << l):
    memo = set()
    b=i
    c = 1
    j=0
    for k,v in primes.items():
        if b & 1<<j:
            c *= k
            for q in v:
                memo.add(q)
        j += 1
    if len(memo)==n:
        ans.append(c)

print(min(ans))
