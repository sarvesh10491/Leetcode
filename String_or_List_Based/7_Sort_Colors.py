# Linear time in-place implementation
#--------------------------------------

''' Algorithm :
i => Loop pointer to traverse all numbers in array
zp => Pointer to track last position in zeros
tp => Tail pointer to track first position in 2s

Whenever we hit 2, we switch 0s & 2s and update respective pointers. 1s will remain in middle & array will get sorted.

'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1: return
        
        i,zp,tp = 0,0,len(nums)-1
        
        while i<=tp:
            if nums[i]==0:
                nums[zp],nums[i] = nums[i],nums[zp]
                zp += 1
                i += 1
            elif nums[i]==2:
                nums[tp],nums[i] = nums[i],nums[tp]
                tp -= 1
            else:
                i += 1