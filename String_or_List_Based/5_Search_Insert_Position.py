# Binary search implementation
#--------------------------------

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0 or (len(nums)==1 and nums[0]>=target): return 0     # Case : Empty array or 1 element in array which is greater than or equal to target
        if len(nums)==1 and nums[0]<target: return 1                        # Case : 1 element in array which is smaller than target
        
        lt,rt = 0,len(nums)-1
        
        while lt < rt:
            if rt-lt == 1:      # Case : left & right pointers are 1 position apart
                if nums[lt]>=target: return lt
                elif nums[rt]>=target: return rt
                else: return rt+1
                
            mid = lt + (rt-lt)//2
            
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                rt = mid
            else:
                lt = mid+1
            
            if lt==rt:            # Case : left & right pointers are on same element
                if nums[lt]>=target: return lt
                else: return lt+1
            
                    
                
            
                