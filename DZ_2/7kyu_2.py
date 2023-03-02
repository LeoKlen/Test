# https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/python
def generate_shape(n):
    ans=''
    for i in range(n):
        ans += '+' * n + '\n'
    ans = ans[:-1]
    return ans
