d = {}

l = [1, 2, 3, 4, 5]

for i in l:
    d[i] = d.get(i, 0) + 1  

print(d)