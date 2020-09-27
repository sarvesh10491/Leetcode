''' Algorithm :
Create 4 pointers to track boundaries of matrix.
In every iteration we will swap respective 4 numbers in ratated position in same ring & make our way inwards.

'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        tp,bt,lt,rt = 0,len(matrix)-1,0,len(matrix[0])-1
        ring = 0
        
        while tp<=bt and lt<=rt:
            for i in range(lt,rt):
                i -= ring                               # To ensure we cover all numbers in row/column in current ring from 0 to excluding last
                tmp = matrix[tp][lt+i]                  # Save top row position number to move to respective right column position in current ring
                matrix[tp][lt+i] = matrix[bt-i][lt]     # Move left column number to respective top row position in current ring
                matrix[bt-i][lt] = matrix[bt][rt-i]     # Move bottom row number to respective left column position in current ring
                matrix[bt][rt-i] = matrix[tp+i][rt]     # Move right column number to respective bottom row position in current ring
                matrix[tp+i][rt] = tmp
            
            tp += 1
            bt -= 1
            lt += 1
            rt -= 1
            ring += 1