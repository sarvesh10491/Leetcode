class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        i = len(triangle)-2
        while i >= 0:
            j = 0
            k = 0
            while j<len(triangle[i]):
                triangle[i][j] = min(triangle[i][j]+triangle[i+1][k] , triangle[i][j]+triangle[i+1][k+1])
                j += 1
                k += 1
            i -= 1
        return triangle[0][0]