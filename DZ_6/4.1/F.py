listik = []
def modern_print(s):
    
    global listik
    if s not in listik:
        listik.append(s)
        return s
