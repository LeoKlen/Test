def month(n, lg):
    
    ru_month = ['Январь', 'Февраль', 'Март',
                'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
                'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    en_month = ['January', 'February', 'March',
                'April', 'May', 'June', 'July', 'August',
                'September', 'October', 'November', 'December']

    if lg == 'ru': 
        return ru_month[n - 1]
    else:
        return en_month[n - 1]
