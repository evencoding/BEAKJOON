import heapq
from sys import stdin
input = stdin.readline

cards = []
for i in range(int(input())):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    result = 0
    while len(cards) > 1:
        mixCard = heapq.heappop(cards) + heapq.heappop(cards)
        result += mixCard
        heapq.heappush(cards, mixCard)
        
    print(result)