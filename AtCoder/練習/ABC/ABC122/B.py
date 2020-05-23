s=input()
l=len(s)
ans=''
anslen=0
for i in range(l):
    for j in range(i,l):
        ok=True
        for ss in s[i:j+1]:
            if ss not in ['A','C','G','T']:
                ok=False
                break
        if ok:
            if anslen<j-i+1:
                ans=s[i:j+1]
                anslen=j-i+1
print(anslen)
