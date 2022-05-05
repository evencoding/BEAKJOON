from collections import deque
n, k = map(int, input().split())
arr = [0] * 100001
queue = deque([n])

def dfs(queue):
    while queue:
        x = queue.popleft()
        if x == k:
            print(arr[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < len(arr) and not arr[nx]:
                queue.append(nx)
                arr[nx] = arr[x] + 1

dfs(queue)