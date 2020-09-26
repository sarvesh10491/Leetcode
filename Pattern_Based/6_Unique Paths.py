# Recursive solution
#=====================

class Solution(object):
    def helper(self, row, col, memo):
        if row == 0 and col == 0:   # return 1 when we are down to 1 cell
            return 1
        if row < 0 or col < 0:
            return 0
        if (row, col) in memo:
            return memo[(row, col)]
        
        res = self.helper(row - 1, col, memo) + self.helper(row, col - 1, memo)     # count paths in each grid with row down & column down
        memo[(row, col)] = res      # Keep track of visited & counted cells to avoid repeated calculations
        
        return res
        
        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.helper(m-1, n-1, {})





# Combinatorial solution
''' Algorithm :
Irrespective of which path we take, total distance we traverse is m-1 horizontally & (n-1) vertically => (m-1) + (n-1) = m+n-2
Using combinatorial formula, number of ways for combination to select either (m-1) steps out of (m+n-2) OR
select (n-1) steps out of (m+n-2) is given by - 

nCr = n! / ((n-r)!  *r!)
    = (m+n-2))! / ((m-1)! * (n-1)!)

'''
#=========================

class Solution(object):
    def fact(self, n):
        if(n == 0):
            return 1
        else:
            return n*self.fact(n-1)
        
        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return (self.fact(m+n-2)) // (self.fact(m-1) * self.fact(n-1))