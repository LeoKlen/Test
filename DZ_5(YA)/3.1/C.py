L = int(input())
n = int(input())
ans_s = ''

while n != 0:
    s = input()
    list(s)
    for i in range(len(s)):
        if len(s) > L:
            if i == L - 3:
                ans_s += '...'
                break
        ans_s += s[i]
    print(ans_s)
    ans_s = ''
    n -= 1
