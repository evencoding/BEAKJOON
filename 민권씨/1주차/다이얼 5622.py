words = list(input())
alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num = list('22233344455566677778889999')

dic = {}
for match in zip(alpha, num):
    dic[match[0]] = int(match[1])+1

sum = 0
for c in words:
    sum += dic[c]

print(sum)