class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        i,j = 0,0
        
        for i in range(numRows):
            res.append([])
            j=0
            while j<=i:
                if j==0 or i==j:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1] + res[i-1][j])
                j += 1
        
        return res