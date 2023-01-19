class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        max_val = arr[length-1]
        arr[length-1] = -1
        for i in range(length-2,-1,-1):
            temp = arr[i]
            arr[i]=max_val 
            if max_val< temp:
                max_val=temp
        return arr