class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [i,d[target - nums[i]]]
            else:
                d[nums[i]] = i