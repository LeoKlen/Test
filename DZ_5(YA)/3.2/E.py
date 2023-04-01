N = int(input())
M = int(input())
Nset = set()
listik = []

for i in range(N + M):
    s = input()
    listik.append(s)
    Nset.add(s)
n = 0
for i in Nset:
    if listik.count(i) == 1:
        n = n + 1

if n == 0:
    print('Таких нет')
else:
    print(n)
