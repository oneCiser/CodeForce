from sys import stdout, stdin
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

case = inp()
res = ['' for i in range(case)]
for _ in range(case):
    n = inp()
    array = sorted(li())
    first = array[n:]
    second = array[:n]
    array[::2] = first
    array[1::2] = second
    res[_] = ' '.join(str(x) for x in array)
[pr(x) for x in res]
