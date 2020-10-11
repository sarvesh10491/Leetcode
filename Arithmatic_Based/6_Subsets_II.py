class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        x = len(nums)
        res = []
        for i in range(1<<x):
            tmp = []
            for j in range(x):
                if i & (1<<j):
                    tmp.append(nums[j])
            tmp.sort()
            if tmp not in res:
                res.append(tmp)
            
        return res
