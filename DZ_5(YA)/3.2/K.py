qty = int(input())
listik = []
qty_one_fam = 0

for i in range(qty):
    s = input()
    listik.append(s)

sett = list(set(listik))

for i in range(len(sett)):
    if listik.count(sett[i]) == 1:
        qty_one_fam += 1
print(qty - qty_one_fam)
