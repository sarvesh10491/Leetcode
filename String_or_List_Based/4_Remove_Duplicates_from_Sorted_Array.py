# Implementation with dictionary
#--------------------------------

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        i = 0
        
        for t in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
                i += 1
            else:
                del nums[i]
        return len(nums)

# Implementation with two pointers
#-----------------------------------
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0 or len(nums)==1: return len(nums)
        
        i,r = 0,1
        for t in range(1,len(nums)):
            if nums[i]==nums[r]:
                del nums[r]
            else:
                i = r
                r += 1
        return len(nums) 
                
                