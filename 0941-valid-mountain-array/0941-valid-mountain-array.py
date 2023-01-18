class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        size=len(arr)
        if size <3:
            return False
        left = 0
        right = size - 1
        while (left < size- 2 and arr[left] < arr[left + 1]):
            left+=1
        
        while (right > 1 and arr[right] < arr[right - 1]) :
            right-=1
        
        return left == right