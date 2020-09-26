# Dynamic programming solution
''' Algorithm :
grid is initialized to 0
We will set 1st row & column to 1 starting from top left cell of grid.
If current cell is obstacle, then we dont need to calculate paths leading upto this cell leaving it 0.
Then for each remaining non-obstacle cell, we will calculate paths possible from that cell by adding available paths from cell row down & column down.
The final value in right bottom cell of grid will be total paths which is expected answer.

obstacle matrix
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

For m=3 & n=3, dp table in end will look like below.
[
[ 1 1 1]
[ 1 0 1]
[ 1 1 2]
]
The function returns value in the right down corner: 28

'''
#=========================

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]   # Empty dp table
        k = min(m,n)    # Select min of rows or columns to iterate over

        for d in range(k):
            if d == 0:  # We will set 1st row & column to 1
                for i in range(d,m):
                    if obstacleGrid[i][d]==1:
                        break
                    dp[i][d] = 1
                for j in range(d,n):
                    if obstacleGrid[d][j]==1:
                        break
                    dp[d][j] = 1
            else:
                for i in range(d,m):
                    if obstacleGrid[i][d]!=1:
                        dp[i][d] = dp[i - 1][d] + dp[i][d - 1]
                for j in range(d,n):
                    if obstacleGrid[d][j]!=1:
                        dp[d][j] = dp[d - 1][j] + dp[d][j - 1]

        return dp[m - 1][n - 1]
        