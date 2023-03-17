#https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
def to_camel_case(text):
    l=0
    r=1
    if not text:
        return text
    s=text[0]
    #print(text)
    

    while r!=len(text):
        if text[r] == '_' or text[r] == '-':
            r+=1

            s+=text[r].capitalize()

            continue
        if s[len(s)-1]==text[r].upper():
            r+=1
            continue
        else:
            s+=text[r]
            r+=1
    return s
        
