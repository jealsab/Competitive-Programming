class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()                      
        result = []
        def combine_sum_2(nums, start, path, result, target):
            if not target:
                result.append(path)
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if nums[i] > target:
                    break
                combine_sum_2(nums, i + 1, path + [nums[i]], result, target - nums[i])
        combine_sum_2(candidates, 0, [], result, target)
        return result