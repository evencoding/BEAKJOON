N = int(input())

def solution():
    global N
    if N < 100:
        cnt = N
        print(N)
    else:
        cnt = 99
        for i in range(100, N+1):
            num = str(i)
            if int(num[1])-int(num[0]) == int(num[2])-int(num[1]):
                cnt += 1
        print(cnt)

solution()