def split_numbers(s):
    ans = s.split(' ')
    for i in range(len(ans)):
        ans[i] = int(ans[i])
    
    return tuple(ans)
