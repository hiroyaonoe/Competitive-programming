s=input()
t=input()
if (s==t[:-1])&(len(t)-len(s)==1):
    print("Yes")
else:
    print("No")