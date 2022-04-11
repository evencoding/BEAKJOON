from sys import stdin
input = stdin.readline

N = int(input())
arr = list(map(int, input().split()))

compression = sorted(list(set(arr)))
dic = {compression[i] : i for i in range(len(compression))}

for i in arr:
    print(dic[i], end=' ')