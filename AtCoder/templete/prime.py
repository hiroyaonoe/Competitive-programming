# 約数を列挙 Order(sqrt(n))
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


# 素数判定
def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3 or num == 5:
        return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False

    # 疑似素数(2でも3でも5でも割り切れない数字)で次々に割っていく
    prime = 7
    step = 4
    num_sqrt = math.sqrt(num)
    while prime <= num_sqrt:
        if num % prime == 0:
            return False
        prime += step
        step = 6 - step

    return True


# num以下の素数列挙
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


# 素因数分解(make_prime_list,math.floorが必要)
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


# 約数の個数(prime_factorizationが必要)
def search_divisor_num(num):
    if num < 0:
        return None
    elif num == 1:
        return 1
    else:
        divisor_num = 1
        dict_fact = prime_factorization(num)
        for value in dict_fact.values():
            divisor_num *= (value + 1)
        return divisor_num


# 階乗数の約数の個数(make_prime_list,defaultdict,math.ceil,math.sqrt)
def search_divisor_num_of_factorial_num(num):
    if num <= 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        # 素数とその個数を入れていく
        dict_counter = defaultdict(int)
        # メモ用のdict
        dict_memo = defaultdict(list)

        for a_num in range(2, num + 1):
            num_sqrt = math.ceil(math.sqrt(a_num))
            prime_list = make_prime_list(num_sqrt)

            # メモ用のdictに入れるためのkeyを残しておく
            now_num = a_num

            for prime in prime_list:
                while a_num % prime == 0:
                    # メモ内にある場合、そこから全部移して、移し終わったらループを抜ける
                    if a_num in dict_memo:
                        for memo in dict_memo[a_num]:
                            dict_counter[memo] += 1
                            dict_memo[now_num].append(memo)

                        a_num = 1

                    else:
                        dict_counter[prime] += 1
                        dict_memo[now_num].append(prime)
                        a_num //= prime

            if a_num != 1:
                dict_counter[a_num] += 1
                dict_memo[now_num].append(a_num)

        divisor_num = 1
        dict_fact = dict(dict_counter)
        for value in dict_fact.values():
            divisor_num *= (value + 1)

        return divisor_num


# A以下の数がN個与えられる。全て素因数分解せよ。
class SpeedPrime:
    # a以下の各数の最小の素因数を記録(エラトステネスのふるい)
    def __init__(self, a):
        self.d = [i for i in range(a+1)]

        i=2
        while i*i<=a:
            if self.d[i]==i:
                j=i*i
                while j<=a:
                    if self.d[j]==j:
                        self.d[j]=i
                    j+=i
            i+=1

    # nを高速素因数分解
    def fac(self, n):
        ret = dict()
        while n!=1:
            prime=self.d[n]
            if prime in ret:
                ret[prime]+=1
            else:
                ret[prime]=1
            n=n//prime
        return ret