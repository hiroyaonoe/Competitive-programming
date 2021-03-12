import input
import solve0310

name = "0023"

n, x, y, r = input.read_input(name)
ret = solve0310.one(n, x, y, r)

with open("ded8fd3366b4ff0b0d7d053f553cdb84/tools/out/"+name+".txt", "w") as f:
    for (a, b, c, d) in ret:
        f.write("{} {} {} {}\n".format(a, b, c, d))