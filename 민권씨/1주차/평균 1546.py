N = int(input())
object = list(map(int, input().split()))

M = max(object)

for i in range(N):
    object[i] = object[i] / M * 100

print(sum(object)/N)