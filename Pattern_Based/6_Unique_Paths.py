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




# Dynamic programming solution
''' Algorithm :
We will set 1st row & column to 1 starting from top left cell of grid.
Then for each remaining cell, we will calculate paths possible from that cell by adding available paths from cell row down & column down.
The final value in right bottom cell of grid will be total paths which is expected answer.

For m=3 & n=7, dp table in end will look like below.
[
[ 1 1 1 1 1 1 1]
[ 1 2 3 4 5 6 7]
[ 1 3 6 10 15 21 28]
]
The function returns value in the right down corner: 28

'''
#=========================

class Solution:
    def uniquePaths(self, m, n):
        dp = [[None for _ in range(n)] for _ in range(m)]   # Empty dp table
        k = min(m,n)    # Select min of rows or columns to iterate over

        for d in range(k):
            if d == 0:  # We will set 1st row & column to 1
                for i in range(d,m):
                    dp[i][d] = 1
                for j in range(d,n):
                    dp[d][j] = 1
            else:
                for i in range(d,m):
                    dp[i][d] = dp[i - 1][d] + dp[i][d - 1]
                for j in range(d,n):
                    dp[d][j] = dp[d - 1][j] + dp[d][j - 1]

        return dp[m - 1][n - 1]