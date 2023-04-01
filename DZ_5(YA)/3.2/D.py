N = int(input())
M = int(input())
Nset = set()
Mset = set()

for i in range(N):
    s = input()
    Nset.add(s)
for i in range(M):
    s = input()
    Mset.add(s)
ans = Nset & Mset
if ans == set():
    print('Таких нет')
else:
    print(len(ans))
