class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zr = set()
        zc = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i not in zr: zr.add(i)
                    if j not in zc: zc.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zr or j in zc:
                     matrix[i][j] = 0