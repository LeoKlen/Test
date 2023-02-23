# https://www.codewars.com/kata/57cff961eca260b71900008f/train/python
def is_vow(inp):
    vow = ['a', 'e', 'i', 'o', 'u']
    for n in range(len(inp)):
        for m in vow:
            if ord(m) == inp[n]:
                inp[n] = m
    return inp
