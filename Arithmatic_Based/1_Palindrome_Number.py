# Implementation without converting integer to string one liner solution {return list(str(x))==list(str(x))[::-1]}

'''Algorithm :
We build integer in reverse order from end till we reach middle.

Strip last digit.
In every iteration multiply number reversed so far from end by 10 & add last digit of remaining number in this iteration.
If reversed number so far is equal to remaining number(even digits in integer case) or if reversed number so far becomes greater to remaining number(odd digits in integer case),
we have reached middle. 
Compare reversed number with original number
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x==0: return True
        if x<0 or x%10==0: return False     # Case : Negative numbers or numbers ending with 0
        
        orgx = x
        revx = 0
        i = 0
        
        while x>0:
            lastd = x%10
            x = x//10
            revx = revx * 10 + lastd
            if revx>=x:
                if revx==x or revx//10==x:
                    return True
                else:
                    return False
            i += 1