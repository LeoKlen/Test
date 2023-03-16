#https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
def to_camel_case(text):
    if not text:
        return ''
    
    ans = ''
    for i in ['-','_']:
        text = text.replace(i,' ')
    text = text.split(' ')
    ans+=text[0]
    for i in range(1,len(text)):
        ans+=text[i].capitalize()
    return ans
