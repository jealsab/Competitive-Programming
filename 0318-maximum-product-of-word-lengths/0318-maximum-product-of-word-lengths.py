class Solution:
    def maxProduct(self, words: List[str]) -> int:

        
        cmp =[]
        for i in range(len(words)):
            lst =['0']*26
            s = len(words[i])
            for k in range(s):
                lst[ord(words[i][k])%97] = '1'
                    
                
            z = "0b"+"".join(lst)
            z = int(z,2)
            cmp.append(z)

        _max = 0
        for i in range(len(cmp)):
            for j in range(i+1,len(cmp)):
                if cmp[i]&cmp[j]==0:
                    q = len(words[i])*len(words[j])
                    _max=max(_max,q)
        return _max
            
       