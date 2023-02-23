# https://www.codewars.com/kata/5b609ebc8f47bd595e000627/train/python
def solution(arr_val, arr_unit) :
    # your code goes here
    dic = dict(kg = 1, g = 0.001, mg = 0.000001, μg = 0.000000001, lb = 0.453592, m = 1, cm = 0.01, mm = 0.001, μm = 0.000001, ft =  0.3048)
    G = 6.67 * pow(10,-11)
    m1 = arr_val[0] * dic[arr_unit[0]]
    m2 = arr_val[1] * dic[arr_unit[1]]
    r  = arr_val[2] * dic[arr_unit[2]]
    F = (G * m1 * m2) / pow(r,2)
    return F
