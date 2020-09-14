import os
import datetime

url = input("The probrem's URL is ").rstrip()

parse = url.split("/")

contest_name=parse[-3].upper()
probrem_name=parse[-1][-1].upper()

date=datetime.date.today()
datestr=date.strftime("%Y%m%d")

filename=probrem_name+datestr+".py"

path=""
default=("ABC","AGC","ARC")
if contest_name[0:3] in default:
    path+=contest_name[0:3]
else:
    path+="others"

path+=os.sep+contest_name

print(path,filename)
os.makedirs(path,exist_ok=True)
os.chdir(path)

with open(filename,"w") as f:
    f.write("")

print("Done")