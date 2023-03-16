#https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
def unique_in_order(s):
    if not s: 
        return []
    
    ans = [s[0]]
    
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            ans.append(s[i])
        else:
            continue
            
    return ans
