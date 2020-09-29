# Binary search solution implementation
#========================================

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0: 
            return False
        
        row_num,col_num = len(matrix),len(matrix[0])    # Assume matrix as single sorted array if we layout all rows one after another

        begin = 0
        end = row_num * col_num - 1

        while begin <= end:
            mid = (begin + end) / 2
            mid_value = matrix[mid/col_num][mid%col_num]

            if mid_value == target:
                return True
            elif mid_value < target:
                begin = mid+1
            else:
                end = mid-1

        return False