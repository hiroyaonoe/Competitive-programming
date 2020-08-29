

## numの２進数における1の個数を返す
def cntbin(num):
    bin_num = bin(num)[2:]
    count = 0
    for i in bin_num:
            count += int(i)
    return count


# n進数
# n進数のstr型の変数Xを10進数の数字(int型)にして返す．
int(X,n)

# 10進数からn進数へ(n<=10)
def tton(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

# n keta 0 padding
str.zfill(n)