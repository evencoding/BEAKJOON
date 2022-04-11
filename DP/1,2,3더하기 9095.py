N = int(input())

case = [0, 1, 2, 4]

for _ in range(N):
    num = int(input())
    while len(case) <= num:
        case.append(case[-1]+case[-2]+case[-3])
    print(case[num])


