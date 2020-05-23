a,b,h,m=list(map(int,input().split()))

from math import sin,cos,pi,sqrt

hh=2*pi*(h+m/60)/12
mm=2*pi*m/60
rad=hh-mm
l=sqrt(a**2+b**2-2*a*b*cos(rad))

print(l)