

h,m,hh,mm,k=list(map(int,input().split()))

hm=h*60+m
hhmm=hh*60+mm

ans=hhmm-k-hm
print(ans)