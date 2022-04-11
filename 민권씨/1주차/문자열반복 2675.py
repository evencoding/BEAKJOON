N = int(input())

for _ in range(N):
    arr = input().split()
    for c in arr[1]:
        print(c * int(arr[0]), end="")
    print("")