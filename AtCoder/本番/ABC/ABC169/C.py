from math import floor

a,b=input().split()
a=int(a)
b=int(b[:-3]+b[-2:])
#b=int(float(b)*100)
print(int(a*b//100))