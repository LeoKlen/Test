# https://www.codewars.com/kata/597bb84522bc93b71e00007e/train/python
def string_merge(string1, string2, letter):
    part1=''
    part2=''
    find=0
    for let in string1:
        if let != letter:
            part1 = part1 + let
        else:
            break
    for let in string2:
        if let == letter:
            find=1
            part2 = part2 + let 
        if let != letter and find==1:
           part2 = part2 + let 
    ans = part1 + part2
    return ans