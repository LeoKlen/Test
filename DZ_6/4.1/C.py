def number_length(s):
    s = str(s)
    if s[0] == '-':
        s = s[1:]
    return len(str(s))
