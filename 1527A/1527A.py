from sys import stdout, stdin
#------------------ USER DEFINED PROGRAMMING FUNCTIONS ------------------#
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

_n = inp()
res = [0 for i in range(_n)]
for i in range(_n):
    k = inp()
    m = k >> 1
    m =0 if m == 0 else len(bin(m)[2::])
    res[i] = 2**m - 1

[pr(i) for i in res]
    