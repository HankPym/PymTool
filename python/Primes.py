import math

rng = 10000

n = 1
b = 3
flag = "False"
ncount = 1
bcount = 1

while n < rng:
    n = n + 1
    nr = math.floor(((math.factorial(n)%(n + 1)) / n))*((n-1)+2)
    
    for bcount in range(b-2):
        if (b %(bcount+2)) == 0:
            flag = "True"
    if flag == "False":
        br = b
    else:
        br = 0
    flag = "False"
    b = b + 1

    if br != 0:
        print(nr, "         ", br)
