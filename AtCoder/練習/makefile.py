import os
import datetime

url = input("The problem's URL is ").rstrip()

parse = url.split("/")

contest_name=parse[-3].upper()

problem_name=input("The problem name is ").upper()

if len(problem_name)==0:
    problem_name = parse[-1][-1].upper()
if len(problem_name)!=1:
    print("A problem name is one letter!")
    exit()


date=datetime.date.today()
datestr=date.strftime("%Y%m%d")

filename=problem_name+datestr+".py"

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
if os.path.exists(filename):
    print("The file exists!")
    exit()

with open(filename,"w") as f:
    f.write("")

print("Done")