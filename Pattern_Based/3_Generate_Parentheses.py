# Recursive implementation

class Solution(object):
    def combo(self, n, ans, s=0, c=0, p=""):
        if c==n:     # All starting parantheses have been closed with equal numbers of valid closing parantheses for current permutation
            ans.append(p)   # Append latest calulated permutation to final answer list
            return
        if s<n:     # New starting parantheses can be added to start permutation
            self.combo(n, ans, s+1, c, p+"(")
        if c<s:     # New closing parantheses can be added to catch up with starting parantheses count
            self.combo(n, ans, s, c+1, p+")")
            
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self.combo(n, ans)
        return ans
        