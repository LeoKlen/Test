s = input()
while s != '':
    if s[-3:] == '@@@':
        s = input()
        continue
    if s[:2] == '##':
        print(s[2:])
        s = input()
        continue
    print(s)
    s = input()
