non_selfnum = set()

def selfnum(num):
    return num + sum(map(int, str(num)))

for i in range(1, 10001):
    non_selfnum.append(selfnum(i))

for i in range(1, 10001):
    if i not in non_selfnum:
        print(i)

