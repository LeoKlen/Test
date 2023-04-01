s = input()
slist = ''
max_s = 0
max_l = ''
while s != 'ФИНИШ':
    s = s.lower()
    slist += s
    s = input()
slist = slist.replace(' ', '')
for i in range(len(slist)):
    if max_s < slist.count(slist[i]):
        max_s = slist.count(slist[i])
        max_l = slist[i]
print(max_l)
