# Dynamic programming solution
''' Algorithm :

for cells in 1st row & column, path is unidirectional hence minimum path sum will be simply adding min sum till previous cell in same row/column to current cell weight.
Then for each remaining cell, we will calculate minimum possible path from that cell by adding min of paths weights between cell row down & column down.
The final value in right bottom cell of grid will be the minimum sum path which is expected answer.

For below grid, calculated path table will look like
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

[
  [1,4,5],
  [2,7,6],
  [6,8,7]
]
The function returns value in the right bottom corner: 7

'''
#=========================

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
        
        for r in range(1,m):
            for c in range(1,n):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
    
        return grid[m - 1][n - 1]     