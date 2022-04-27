from sys import stdin
input = stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
dict = {}
numList = []

for i in range(N):
    for j in range(len(words[i])):
        if words[i][j] in dict:
            dict[words[i][j]] += 10 ** (len(words[i])-j-1)
        else:
            dict[words[i][j]] = 10 ** (len(words[i])-j-1)

for v in dict.values():
    numList.append(v)

numList.sort(reverse=True)

pows = 9
sum = 0
for n in numList:
    sum += n * pows
    pows -= 1

print(sum)

