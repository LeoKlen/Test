N = int(input())
M = int(input())
listik = []
flag = True

for i in range(N + M):
    s = input()
    listik.append(s)

listik.sort()

for i in listik:
    if listik.count(i) == 1:
        flag = False
        print(i)
if flag:
    print('Таких нет')
