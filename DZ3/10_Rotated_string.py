#https://www.codewars.com/kata/55467aaf72494e3bdc00007f/train/python
def is_rotation(s1,s2):
    
    print("|",s1,"|",s2,"|", sep='')
    
    if(len(s1)!=len(s2) ):
        return False
    if(len(s1)==0 ):
        return True
    j=s2.find(s1[0])
    if(j==-1): 
        return False
    res=True
    for i in range(len(s1)):
        #print("s1[",i,"]=",s1[i]," s2[",j,"]=",s2[j])
        if s1[i]==s2[j]:
            if j==len(s1)-1:
                j=0
                continue
            j+=1
        else:
            res=False
    return res
