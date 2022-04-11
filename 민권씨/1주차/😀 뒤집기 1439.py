S = input()

print(min(len(S.replace('0', ' ').split()), len(S.replace('1', ' ').split())))