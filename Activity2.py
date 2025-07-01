testdic = {'Codingal' : 2, 'Is':2, 'Best':2, 'for': 2, 'Coding':5}

k = 2

res = 0

for key in testdic:
    if testdic[key] == k:
        res += 1

print(res)