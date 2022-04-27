from sys import stdin
input = stdin.readline

A, B = map(int, input().split())
N = int(input())
bookmark = [int(input()) for _ in range(N)]

numList = [abs(A-B)]
for n in bookmark:
    numList.append(abs(B-n)+1)

print(min(numList))