n = int(input())
let = ['а', 'б', 'в']
flag = 'YES'
for i in range(0, n):
    word = input()
    if word[0] not in let:
        flag = 'NO'
print(flag)
