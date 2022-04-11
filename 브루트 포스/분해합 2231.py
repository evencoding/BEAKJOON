N = int(input())

for i in range(N):
    if i == N-1:
        print(0)
        break;
    apart_sum = i
    for j in str(i):
        apart_sum += int(j)
    if apart_sum == N:
        print(i)
        break;