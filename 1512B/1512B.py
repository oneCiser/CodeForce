from sys import stdout, stdin
st=lambda:list(stdin.readline().strip())
li=lambda:list(map(int,stdin.readline().split()))
mp=lambda:map(int,stdin.readline().split())
inp=lambda:int(stdin.readline())
pr=lambda n: stdout.write(str(n)+"\n")
for _ in [0]*inp():
    n = inp()
    m = [st() for _ in [0]*n]
    (i1,j1), (i2, j2) = [(i,j) for i,v in enumerate(m) for j,x in enumerate(v) if '*' == x]
    i2, j2 = (i2 + (i2 == i1))%n , (j2 + (j2 == j1))%n
    m[i2][j2]=m[i2][j1]=m[i1][j2]='*'
    for l in m:
        pr(''.join(v for v in l))
