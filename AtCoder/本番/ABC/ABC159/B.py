s=input()
n=len(s)
ok=True
for i in range(int(n//2)):
    if s[i]!=s[n-i-1]:
        ok=False

for i in range(int((n//2)//2)):
    if s[i]!=s[n//2-i-1]:
        ok=False

for i in range(int((n//2)//2)):
    if s[n//2+1+i]!=s[n-i-1]:
        ok=False

if ok:print("Yes")
else:print("No")