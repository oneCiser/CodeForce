from sys import stdout, stdin
#------------------ USER DEFINED PROGRAMMING FUNCTIONS ------------------#
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
import math

_n = inp()
res = [0 for i in range(_n)]
for _ in range(_n):
    n = inp()
    if n<10:
        res[_] = n
    else:
        digit = int(math.log10(n))
        last =n//10**digit 
        k_is = 1 if int(str(last)*(digit+1))<=n else 0
        number = n//10**digit - 1 + k_is + (digit)*9
        res[_] = number
[pr(_) for _ in res]
     