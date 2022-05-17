n, m = map(int, input().split())
quad = []
for _ in range(n):
    quad.append(input())

mini = []

for k in range(n-7):
    for l in range(m-7):
        minB = 0 # 블랙이 시작일 때
        minW = 0 # 흰색이 시작일 때
        for i in range(k, k+8):
            for j in range(l, l+8):
                if (i+j)%2:
                    if quad[i][j] != "W": minB += 1
                    if quad[i][j] != "B": minW += 1
                else:
                    if quad[i][j] != "B": minB += 1
                    if quad[i][j] != "W": minW += 1
        mini.append(minB)
        mini.append(minW)

print(min(mini))