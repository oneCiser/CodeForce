from sys import stdout, stdin
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")

_n = inp()
res = ['YES' for i in range(_n)]
for _ in range(_n):
    days = inp()
    tasks = st()
    if days > 2:
        work_in = set()
        current = 1
        while current < days:
            if tasks[current] in work_in:
                res[_] = 'NO'
                break
            if tasks[current] != tasks[current - 1]:
                work_in.add(tasks[current - 1])
            current += 1
[pr(_) for _ in res]


