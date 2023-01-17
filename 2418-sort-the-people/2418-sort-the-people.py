class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for i in range (len(heights)-1):
            max_num=i
            for j in range(i+1,len(heights)):  
                if heights[max_num]<heights[j]:
                    max_num=j
            names[i],names[max_num]=names[max_num],names[i]
            heights[i],heights[max_num]=heights[max_num],heights[i]

        return names
    