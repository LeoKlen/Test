# https://www.codewars.com/kata/56d6b7e43e8186c228000637/train/python
def colour_association(arr):
    #your code here
    for i in range(len(arr)):
        arr[i] = dict([arr[i]])
    return arr