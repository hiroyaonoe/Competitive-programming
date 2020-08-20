n = int(input())
ans =""
while True:

    i = n%26
    if i == 0:i = 26
    n = (n-1) // 26
    mo = ord("a")+(i-1)

    ans = chr(mo) + ans
    if n == 0:
        break

print(ans)

