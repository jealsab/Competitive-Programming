class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
      
        low =0
        high = len(arr)-1
        
        while low <= high:
            mid = (low+high)//2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid-1] < arr[mid] and arr[mid] < arr[mid + 1]:
                low += 1
            elif arr[mid-1] > arr[mid] and arr[mid] > arr[mid + 1]:
                high -= 1
   