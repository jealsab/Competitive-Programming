class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i=j=0
        res=0
        dict={}
        while j<len(fruits):
            dict[fruits[j]]=j
            if len(dict)>=3:
                lri=min(dict.values())
                dict.pop(fruits[lri])
                i=lri+1
            res=max(res,j-i+1)
            j+=1
        return res