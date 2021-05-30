import numpy as np
import sys
sys.setrecursionlimit(2000000000)

def partition(lst, pivot):
    """Modifired partition algorithm in section 7.1"""
    pivot_idx = None
    for idx, value in enumerate(lst):
        if value == pivot:
            pivot_idx = idx
    if pivot_idx is None:
        print("err")
    lst[pivot_idx], lst[-1] = lst[-1], lst[pivot_idx]
    pivot = lst[-1]
    i = -1
    for j, val in enumerate(lst[:-1]):
        if val <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[-1] = lst[-1], lst[i + 1]
    return i + 1


def select(lst, i):
    """Selection in linear time"""
    if len(lst) == 1:
        return lst[0]
    split_lists = [lst[i * 5: (i + 1) * 5] for i in range((len(lst) + 4) // 5)]
    split_list_medians = [
        sorted(split_list)[(len(split_list) - 1) // 2]
        for split_list in split_lists
    ]
    x = select(split_list_medians, (len(split_list_medians) - 1) // 2)
    k = partition(lst, x)
    if i == k:
        return x
    elif i < k:
        return select(lst[:k], i)
    else:
        return select(lst[k + 1:], i - (k + 1))


def median_linear(lst):
    """Calculate median by selection algorithm"""
    return select(lst, (len(lst) - 1) // 2)


n, k = list(map(int, input().split()))

a = []
m = n - (k * k) // 2

for i in range(n):
    ai = list(map(int, input().split()))
    a.append(ai)

ad = np.array(a)

import time
start = time.time()
now = time.time()

ans = 1 << 32
for i in range(n - k + 1):
    for j in range(n - k + 1):
        print(time.time() - now)
        now = time.time()
        l = ad[i:i+k][j:j+k].flatten()
        mid = median_linear(l)
        if ans > mid:
            ans = mid

print(mid)
print(time.time()-start)
