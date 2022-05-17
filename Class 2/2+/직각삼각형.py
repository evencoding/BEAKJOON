while 1:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    idx = n.index(max(n))
    square_sum = 0
    for i in range(3):
        if i == idx:
            continue
        square_sum += n[i]**2
    if n[idx]**2 == square_sum:
        print('right')
    else:
        print('wrong')
