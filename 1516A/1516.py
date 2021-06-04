from sys import stdout, stdin
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
for _ in range(inp()):
    n, k = mp()
    a = li()
    i = 0
    while k and i < n:
        m = min(a[i], k)
        a[i] -= m
        a[-1] += m
        k -= m
        i += 1
    pr(' '.join(str(v) for v in a))
