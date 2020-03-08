s=input()

test=["hi"*i for i in range(10)]

ans="No"
for t in test:
    if s==t:
        ans="Yes"
print(ans)