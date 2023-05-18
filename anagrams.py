import sys

if len(sys.argv) < 2:
    print('Please enter a word')
    sys.exit()

res = []

with open('words_alpha copy 2.txt', 'r') as f:
    for word in f.readlines():
        if sorted(word.strip()) == sorted(sys.argv[1]) and word.strip() != sys.argv[1]:
            res.append(word.strip())

print(res)          