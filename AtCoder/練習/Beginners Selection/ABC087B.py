a=int(input())
b=int(input())
c=int(input())
x=int(input())
cnt=0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if x == 500*i+100*j+50*k:cnt+=1
print(cnt)
'''
coinA=min(a,x//500)
coinB=min(b,(x-coinA*500)//100)
coinC=min(c,(x-coinB*100)//50)
cnt=0
changeB=coinB
changeC=coinC
if 500*coinA+100*coinB+50*coinC>=x:
    while coinA>=0:
        while 0<=changeB<=b:
            if 0<=changeC<=c:
                cnt+=1
            changeB-=1
            changeC+=2
        changeB=coinB
        changeC=coinC
        coinA-=1
        changeB+=5
print(cnt)
'''