class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = []
        for i in range(1,n+1):
            nums.append(i)
    
        x = len(nums)
        res = []
        
        for i in range(1 << x):
            tmp = []
            for j in range(x):
                if (i & (1 << j)):
                    tmp.append(nums[j])
            if len(tmp)==k:
                res.append(tmp)
            
        return (res)