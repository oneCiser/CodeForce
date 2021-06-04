from sys import stdout, stdin
#------------------ USER DEFINED PROGRAMMING FUNCTIONS ------------------#
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

_n = inp()
res = [0 for _ in range(_n)]
for _ in range(_n):
    size = inp()
    array = li()
    count = array.count(min(array,key=int))
    res[_] = size - count
for _ in res:
    pr(_)
