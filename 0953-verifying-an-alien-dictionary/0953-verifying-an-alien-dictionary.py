class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict={}
        for i in range (len(order)):
            dict[order[i]]=i
        print(dict)
        
        for i in range(1,len(words)):
            a = words[i-1]
            b = words[i]
            for j in range(len(a)):
                if j == len(b): 
                    return False
                curr_a = a[j]
                curr_b = b[j]
                idx_a = dict[curr_a] 
                idx_b = dict[curr_b]
                if idx_a < idx_b:
                    break
                if idx_a > idx_b:
                    return False
        return True
        
        
        
        
        
    
#         for i in range (len(words)-1):
#             words1=words[i]
#             words2=words[i+1]
#             if (len(words1))>(len(words2)):
#                 return False
#             for j in range (min(len(words1),len(words2))):
#                 if words1[j]!=words2[j+1]:
#                     if dict[words1[j]]>dict[words2[j]]:
#                         return False
#                     else:
#                         return True 
        