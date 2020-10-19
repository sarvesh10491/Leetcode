class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        if len(matrix)==0:
            return ans
            
        tp, bt, lt, rt = 0,len(matrix),0,len(matrix[0])     # 4 pointers for 4 direction traverse
        
        while lt < rt and tp < bt:
            i,j = tp,lt         # Start with top left
            while j < rt:       # traverse right in current row adding node to ans list
                ans.append(matrix[i][j])
                j += 1
            i += 1           
            j -= 1              
            tp += 1             # Increment tp for start of next round's ring
            
            if bt <= tp:        # check if are done with all rings
                break
            
            while i < bt:       # traverse down in current column adding node to ans list
                ans.append(matrix[i][j])
                i += 1
            rt -= 1             # Move to column behind
            
            if rt <= lt:        # check if are done with all rings
                break
            i -= 1
            j -= 1
            
            while j >= lt:      # traverse left in current row adding node to ans list
                ans.append(matrix[i][j])
                j -= 1
            bt -= 1
            
            if bt <= tp:        # check if are done with all rings
                break
            j += 1
            i -= 1
            
            while i >= tp:      # traverse up in current column adding node to ans list
                ans.append(matrix[i][j])
                i -= 1
            lt += 1
            
        return ans
        