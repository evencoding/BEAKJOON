N = int(input())

cnt = 1
num = 1
idx = 1

while True:
    if N <= num: 
        break
    num = num + idx * 6
    idx += 1
    cnt += 1

print(cnt)




