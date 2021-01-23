import os

url = input("The Contest URL is ").rstrip()
parse = url.split("/")
contest_name=parse[-1].upper()

path=""
default=("ABC","AGC", "ARC")
if contest_name[0:3] in default:
    path+=contest_name[0:3]
else:
    path+="others"

num=int(input("The number of probrems is "))

path+=os.sep+contest_name

print(path,num)
os.makedirs(path)
os.chdir(path)
for i in range(num):
    filename=chr(ord("A")+i)+".py"
    with open(filename,"w") as f:
        f.write("")

print("Done")