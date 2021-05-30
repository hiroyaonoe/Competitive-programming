n = int(input())

memo = [set() for i in range(n+1)]

if n % 2:
    exit()

for i in range(2, n+1, 2):
    if i == 2:
        memo[2].add("()")
    else:
        for j in range(2, i-1, 2):
            for left in memo[j]:
                for right in memo[i-j]:
                    memo[i].add(left+right)
        for s in memo[i-2]:
            memo[i].add("()" + s)
            memo[i].add(s + "()")
            memo[i].add("(" + s + ")")

ans = sorted(list(memo[n]))
for i in ans:
    print(i)
