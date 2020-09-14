class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0: return ""
        if len(strs)==1: return strs[0]
        
        pref = ""
        wt = 1
        while True:
            tpref = strs[0][:wt]
            for lt in range(1,len(strs)):
                if strs[lt][:wt]!=tpref:
                    return pref
            pref = tpref
            
            wt += 1
            if wt>len(strs[0]):
                return pref
