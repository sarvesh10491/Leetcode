''' Algorithm :
If n=0 stairs, Possible Ways => 0 [Total Ways- 0]
If n=1 stairs, Possible Ways => 1 [Total Ways- 1]
If n=2 stairs, Possible Ways => 1-1, 2 [Total Ways- 2]
If n=3 stairs, Possible Ways => 1-1-1, 2-1, 1-2 [Total Ways- 3]
If n=4 stairs, Possible Ways => 1-1-1-1, 1-1-2, 2-1-1, 2-2,1, 1-2-1 [Total Ways- 5]

Thus answer follows Fibonacci series which is all we need to implement to get answer.

'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res,pre,nxt = 0,1,2
        
        if n==1: 
            return 1
        if n==2: 
            return 2
        else:
            for i in range(3,n+1):
                res = pre + nxt
                pre,nxt = nxt,res
        
        return res
          