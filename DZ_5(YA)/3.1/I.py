s = input()
while s != '':
    i = s.find('#')
    if i != 0:
        print(s[:i])
    if i == -1:
        print(s)
    s = input()
