class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = -1
        lt,rt = 0,len(height)-1
        
        while lt<rt:
            area = min(height[lt],height[rt]) * (rt-lt)
            maxarea = max(maxarea,area)
            
            if height[lt]<height[rt]:   # Case : Right end boundary is taller
                lt += 1     # Move left end boundary by 1 to right
                while lt<rt and height[lt-1]>=height[lt]:   # Keep moving to right until you find taller left end boundary than last left end boundary
                    lt += 1
            else:                       # Case : Left end boundary is taller
                rt -= 1     # Move right end boundary by 1 to left
                while lt<rt and height[rt+1]>=height[rt]:      # Keep moving to left until you find taller right end boundary than last right end boundary
                    rt -= 1
                    
        return maxarea
        