import heapq
from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
gems = []
for _ in range(N):
    heapq.heappush(gems, list(map(int, input().split())))

bag = [int(input()) for _ in range(K)]
bag.sort(reverse=True)
maxHeap = []
sum = 0
for _ in range(K):
    weight = bag.pop()
    while gems and weight >= gems[0][0]:
        info, value = heapq.heappop(gems)
        heapq.heappush(maxHeap, -value)
    if maxHeap:
        sum -= heapq.heappop(maxHeap)

print(sum)

