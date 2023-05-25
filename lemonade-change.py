class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        dic = defaultdict(int)
        
        for bill in bills:
            if bill==5:
                dic[5]+=1
            elif bill==10:
                dic[10]+=1
                if dic[5]>=1:
                    dic[5]-=1
                    
                else:
                    return False
            else:
                if dic[5]>=1 and dic[10]>=1:
                    dic[10]-=1
                    dic[5]-=1
                elif dic[5]>=3 :
                    dic[5]-=3
                    
                
                else:
                    return False
        return True