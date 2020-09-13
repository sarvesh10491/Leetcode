class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        if len(s)==0 or len(s)==1:
            return len(s)
        cur_l, max_l = 1,1
        r,f = 0,1
        d = {}
        d[s[r]] = 1
        
        while f<len(s):
            if s[f] not in d:
                cur_l += 1
                d[s[f]] = 1
                f += 1
                
            else:
                max_l = max(max_l,cur_l)
                cur_l = 1
                r += 1
                f = r+1
                d = {}
                d[s[r]] = 1
                
        return max(max_l,cur_l)