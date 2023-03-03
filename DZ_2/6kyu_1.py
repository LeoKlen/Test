# https://www.codewars.com/kata/593c0ebf8b90525a62000221/train/python
def group_groceries(groceries):
    categories = {'fruit':[], 'meat':[], 'other':[], 'vegetable':[]}
    # добавление в словарь
    for item in groceries.split(','):
        #print("item=", item)
        key, value = item.split('_')
        #print("key=", key, "  value=", value)
        if key not in categories:
            categories['other'].append(value)
        else:
            categories[key].append(value)

    #вывод в строку
    ans = ''
    #print("categories=", categories)
    for category in categories:
       ans += category + ':' + ','.join(sorted(categories[category])) + '\n'
    
    #return ans
    return ans[:-1]
