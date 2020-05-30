h = int(input())
w = int(input())
n = int(input())

hw = max(h, w)

ans = (n + hw - 1) // hw

print(ans)