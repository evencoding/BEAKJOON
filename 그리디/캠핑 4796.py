case = 1
while True:
    L, P, V = map(int, input().split())
    if V == 0:
        break
    result = V // P * L
    result += V % P if V % P <= L else L
    print(f'Case {case}: {result}')
    case += 1