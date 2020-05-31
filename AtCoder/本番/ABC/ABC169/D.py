# n=int(input())
#
# from math import sqrt
#
# div = int(sqrt(n))
# ans=0
# for i in range(2,div+1):
#     if n%i==0:
#         ans+=1
#         n=int(n//i)
#
# if ans==0:ans=1
#
# if n==1:ans=0
# print(ans)



n=int(input())

import math

def make_prime_list_2(num):
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

def prime_factorization_2(num):
    if num <= 1:
        return False
    else:
        num_sqrt = math.floor(math.sqrt(num))
        prime_list = make_prime_list_2(num_sqrt)

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

l=prime_factorization_2(n)
ans=0

if l==False:pass
else:

    for div,nums in l.items():
        num=nums
        num-=1
        i=2
        while num>=0:
            ans+=1
            num-=i
            i+=1


print(ans)