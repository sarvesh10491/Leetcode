class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        op = ['(','[','{']

        for i in range(len(s)):
            if s[i] in op:      # Case : opening parantheses
                stack.append(s[i])
            else:
                if len(stack)==0:   # Case : Closing parantheses but stack is empty
                    return False
                else:
                    if (s[i]==')' and stack[-1]=='(') or (s[i]==']' and stack[-1]=='[') or (s[i]=='}' and stack[-1]=='{'):  # Case : Closing parantheses match top of stack opening parantheses
                        del stack[-1]
                    else:   # Case : Closing parantheses does not match top of stack opening parantheses
                        return False

        if len(stack)==0: return True
        else: return False  # Case : Trailing closing parantheses in stack
        
        