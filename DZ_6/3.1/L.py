menu = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

days = int(input())
ostatok = days % 5
full = days // 5

ans = menu * (days // 5) + menu[:days % 5]

print("\n".join(ans))
