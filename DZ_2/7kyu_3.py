# https://www.codewars.com/kata/563a8656d52a79f06c00001f/train/python
def is_valid(idn):
    inti = '0123456789'
    sym = '][*\>."@`~=/,?(#^){}|+;:"'
    
    
    if idn == '':
        return False 
    for i in idn:
        for s in sym:
            if i == s:
                return False
    if idn[0]=='!' or idn.count(' ')>0 or idn.count('-')>0 or inti.count(idn[0])>0 :
        return False
    else:
        return True