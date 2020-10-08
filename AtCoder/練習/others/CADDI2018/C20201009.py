n,p=list(map(int,input().split()))
import math
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


def prime_factorization(num):
    if num <= 1:
        return False
    else:
        num_sqrt = math.floor(math.sqrt(num))
        prime_list = make_prime_list(num_sqrt)

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

if p==1:
    print(1)
    exit()

l=prime_factorization(p)

ans=1
for k,v in l.items():
    ans*=k**(v//n)

print(ans)