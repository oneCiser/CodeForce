from sys import stdout, stdin
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
for _ in range(inp()):
    n = inp()
    a = li()
    index = 0
    while n:
        if a[index]**(0.5)%1:
            pr('YES')
            break
        index += 1
        n -= 1
    if not n:
        pr('NO')