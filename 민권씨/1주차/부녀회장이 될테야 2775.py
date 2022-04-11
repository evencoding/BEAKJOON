from sys import stdin
input = stdin.readline

N = int(input())
for _ in range(N):
    k = int(input())
    n = int(input())

    mtx = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(1, n+1):
        mtx[0][i] = i
    for i in range(1, k+1):
        for j in range(1, n+1):
            mtx[i][j] = sum(mtx[i-1][1:j+1])
    
    print(mtx[k][n])

