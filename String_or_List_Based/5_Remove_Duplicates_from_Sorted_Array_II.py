class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenn = len(nums)
        if lenn==0: return 0
        i,c = 0,0
        h = dict()
        
        while c<lenn:
            # print(c,i)
            if nums[i] not in h: 
                h[nums[i]] = 1
                i += 1
            elif h[nums[i]]==1:
                h[nums[i]] = 2
                i += 1
            else:
                del nums[i]
            c += 1
            
        return len(nums)