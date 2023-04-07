s = input()
s = s.lower()
i = 0
j = len(s) - 1
ans = 'YES'

while i < j:
    if s[i] == ' ':
        i += 1
    if s[j] == ' ':
        j -= 1
    if s[i] != s[j]:
        ans = 'NO'
        break
    i += 1
    j -= 1
print(ans)
