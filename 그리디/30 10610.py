sortedNum = sorted(list(input()), reverse=True)
print(''.join(sortedNum) if sortedNum[-1] == '0' and not sum(map(int, sortedNum))%3 else -1)