class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        l = []
        for i in range(len(nums)-1,-1,-1):
            _min = min(nums[:i+1])
            l.append(_min)
        l.reverse()
        print(l)

        r =[]
        for i in range(len(nums)):
            _max = max(nums[i:])
            r.append(_max)
            print(r)
        # r.reverse()
        print(r)

        for i in range(len(nums)):
            if l[i]<nums[i]<r[i]:
                return True
        return False