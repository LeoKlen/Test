N = int(input())

for i in range(N):
    s = input()
    qty = 1 + s.find('зайка')
    if qty == 0:
        print('Заек нет =(')
        continue
    print(qty)
