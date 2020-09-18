# Linear implementation
#------------------------

''' Algorithm :
Starting with position 1, we move along storing running sum in that position in array.
For every position, we check if previous number was positive. If yes, then we add current number to that which represents running sum since of current chain.
If its negative, we skip as ww are entering in new chain.
In the end, we return max in the nums array which will have max subarray sum.

'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
                
        return max(nums)