from sys import stdin
import heapq
input = stdin.readline

N = int(input())
leftHeap = []
rightHeap = []
for _ in range(N):
    num = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)
    
    if rightHeap and -leftHeap[0] > rightHeap[0]:
        tmp = -heapq.heappop(leftHeap)
        heapq.heappush(leftHeap, -heapq.heappop(rightHeap))
        heapq.heappush(rightHeap, tmp)

    print(-leftHeap[0])
