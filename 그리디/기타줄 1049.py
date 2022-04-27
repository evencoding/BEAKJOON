from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
package = []
piece = []
for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    piece.append(b)

res = min((N // 6) * min(package), (N // 6) * min(piece) * 6)
res += min((N % 6) * min(piece), min(package))

print(res)