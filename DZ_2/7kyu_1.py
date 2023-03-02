# https://www.codewars.com/kata/598f76a44f613e0e0b000026/train/python
def sum_of_integers_in_string(s):
    chisli = []
    word =''
    slog = []
    ans = 0
    print(s)
    for i in s:
        print(i)
        if i.isdigit()==True :
            chisli.append(i)
        else:
            chisli.append('')
    for i in chisli:
        if i != '':
            word+=i
        elif i == '':
            slog.append(word)
            word=''
    slog.append(word)
    for i in slog:
        print('i=', i)
        if i == '':
            pass
        else:
            ans += int(i)
    return ans
