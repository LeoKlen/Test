# https://www.codewars.com/kata/5748838ce2fab90b86001b1a/train/python
import math
def square_area(A):
    # your code here
    S = pow(2 * A / math.pi,2)
    ans = round(S,2)
    return ans
