# https://www.codewars.com/kata/5a4a391ad8e145cdee0000c4/train/python
import math
def has_subpattern(string):
    dick = []
    dickQty = []
    for i in string:
        if dick.count(i) == 0:
            dick.append(i)
            dickQty.append(string.count(i))

    gcd = math.gcd(*dickQty)
    if(gcd>1):
        return True
    else:
        return False
