import time

n=10**5+1

start=time.time()

print(list(range(n,-1,-1)))

mid=time.time()
print(mid-start)

print(list(range(n+1)))

print(time.time()-mid)

l=['0' for i in range(10**5)]
p=' '.join(l)

print(p)



# print('---------')
# a=[]
# start=time.time()
# for i in range(n):
#     a.append(2**i)
# print(time.time()-start)