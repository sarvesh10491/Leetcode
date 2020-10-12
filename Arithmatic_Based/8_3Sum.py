class Solution:
    def threeSum(self, nums):
        d = {}
        if len(nums) < 3:
            return []
        
        nums = sorted(nums)
        for i, num in enumerate(nums):
            l = i+1
            r = len(nums)-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    t = (nums[i],nums[l], nums[r])
                    if t not in d:
                        d[t] = 1
                    if nums[l] == nums[r]:
                        break
                    l += 1
                    r -= 1
        return map(list, d.keys())