listik = []
d = dict()
s = input()

while s != '':
    listik += s.split(' ')
    s = input()
d = dict.fromkeys(listik)
sett = list(d)
for i in range(len(sett)):
    qty = listik.count(sett[i])
    d[sett[i]] = qty
for k, v in d.items():
    print(k, v)
