from sys import stdout, stdin
#------------------ USER DEFINED PROGRAMMING FUNCTIONS ------------------#
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
def mcd(a,b):
    if b == 0:
        return a
    else:
        return mcd(b, a%b)
_n = inp()
res = [0 for i in range(_n)]
for _ in range(_n):
    e = inp()
    MCD = mcd(100,e)
    res[_] = 100 if MCD == 1 else 100//MCD
[pr(i) for i in res]

