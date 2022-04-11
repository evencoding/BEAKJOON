word = input()

for c in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    if c in word:
        word = word.replace(c, "*")

print(len(word))