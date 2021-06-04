from sys import stdout, stdin
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
for _ in range(inp()):
    n, k = mp()
    N = n if n%2 else n - 1 
    if N//2 >= k:
        a = [i + 1 for i in range(n)]
        m = n//2
        a_m = a[:k+1]
        a_M = a[k+1:min(2*k+1,n)]
        a[:min(2*(k+1),n):2] = a_m
        a[1:2*k+1:2] = a_M
        pr(' '.join(str(v) for v in a))
    else:
        pr(-1)