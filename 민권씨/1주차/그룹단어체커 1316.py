N = int(input())
cnt = 0

for _ in range(N):
    word = input()
    arr = word[0]
    for i in range(1, len(word)):
        if word[i] == word[i-1]: 
            continue
        arr += word[i]

    for i, c in enumerate(arr):
        if arr.count(c) > 1: 
            break
        if i == len(arr)-1: 
            cnt += 1

print(cnt)