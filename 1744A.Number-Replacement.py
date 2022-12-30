n=int(input())
for i in range(n):
    l=int(input())
    arr=list(input().split())
    s=input()
    
    m=True
    d={}
    i,j=0,0
    
    while i<l:
        if arr[i] not in d:
            d[arr[i]]=s[j]
        
        else:
            
            if d[arr[i]]==s[j]:
                pass
            else:
                m=False
                break
            
        i+=1
        j+=1
    if m==False:
        print("NO")
    else:
        print("YES")