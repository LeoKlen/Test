# https://www.codewars.com/kata/5865cff66b5699883f0001aa/train/python
def to_time(seconds):
    return str(seconds // 3600) +' hour(s) and ' + str(seconds%3600//60) + " minute(s)"