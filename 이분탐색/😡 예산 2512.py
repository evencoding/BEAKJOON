N = int(input())
area = list(map(int, input().split()))
budget = int(input())

start = 0
end = max(area)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in area:
        if i <= mid:
            sum += i
        else:
            sum += mid
    if sum <= budget:
        start = mid + 1
    else:
        end = mid - 1

print(end)