import os
import sys

dir=""
while dir=="":
    type=int(input("ABC:0 AGC:1 Other:2 ->"))

    if type==0:dir="ABC"
    elif type==1:dir="AGC"
    elif type==2:dir="others"
    else:
        print("Please input 0 or 1 or 2.")


name=input("Contest name is ")
num=int(input("The number of probrems is "))



path=dir+"/"+name
os.makedirs(path)
os.chdir(path)
for i in range(num):
    filename=chr(ord("A")+i)+".py"
    with open(filename,"w") as f:
        f.write("")


