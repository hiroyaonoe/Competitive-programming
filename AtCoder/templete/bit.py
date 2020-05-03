

## numの２進数における1の個数を返す
def cntbin(num):
    bin_num = bin(num)[2:]
    count = 0
    for i in bin_num:
            count += int(i)
    return count