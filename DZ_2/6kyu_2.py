#https://www.codewars.com/kata/597ef546ee48603f7a000057/train/python
def get_most_profit_from_stock_quotes(arr):
    res = 0
    indMax = len(arr)-1
    for n in range(len(arr)-2,-1,-1):
        if arr[n] >= arr[indMax]:
                indMax = n

        res += arr[indMax] - arr[n]
    return res

