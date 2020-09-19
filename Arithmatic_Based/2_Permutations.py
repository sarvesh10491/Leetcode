# Implementation without converting integer to string one liner solution {return list(str(x))==list(str(x))[::-1]}

'''Algorithm :
Recursive approach in which we will create copy of passed list & swap 2 numbers everytime time to generate new permutation.
step variable will be used to track if we used all numbers in list. 
If yes, append current permutation result to ans list for current copy of numbers.

'''

class Solution(object):
    def helper(self, nums, ans, step=0):
        if step==len(nums):
            ans.append(nums)

        for i in range(step, len(nums)):
            nums_cpy = [n for n in nums]
            nums_cpy[step],nums_cpy[i] = nums_cpy[i],nums_cpy[step]
            self.helper(nums_cpy, ans, step+1)

            
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.helper(nums, ans)
        
        return ans