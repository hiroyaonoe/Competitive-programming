n=int(input())
a = list(map(int,input().split()))
sum_a = sum(a)
sum_even = sum(a[0::2])
sum_odd = sum_a-sum_even

b=[]
prev_b = sum_even-sum_odd
for i in range(n):
    b.append(str(prev_b))
    prev_b = a[i]*2-prev_b

print(" ".join(b))