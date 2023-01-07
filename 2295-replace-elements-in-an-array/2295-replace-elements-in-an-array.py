class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dict={}
        for i in range (len(nums)):
            dict[nums[i]]=i
        for a, b in operations:
          idx = dict[a]
          nums[idx] = b
          del dict[a]
          dict[b] = idx

        return nums