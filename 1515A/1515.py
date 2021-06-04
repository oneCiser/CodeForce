from sys import stdout, stdin
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
for _ in range(inp()):
    n, x= mp()
    a = li()
    for i  in range(1,n):
        if sum(a[:i]) == x:
            a[i - 1], a[i] = a[i], a[i - 1]
    if sum(a) == x:
        pr('NO')
    else:
        pr('YES')
        pr(' '.join(str(v) for v in a))