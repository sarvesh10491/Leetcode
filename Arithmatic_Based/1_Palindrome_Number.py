# Implementation without converting integer to string one liner solution {return list(str(x))==list(str(x))[::-1]}

'''Algorithm :
We build integer in reverse order from end till we reach middle.

Strip last digit.
In every iteration multiply number reversed so far from end by 10 & add last digit of remaining number in this iteration.
If reversed number so far is equal to remaining number(even digits in integer case) or if reversed number so far becomes greater to remaining number(odd digits in integer case),
we have reached middle. 
Compare reversed number with remaining number(even digits in integer case) or remaining number with excluding last digit(odd digits in integer case) for palindrome.

1221
rem x       last digit      reversed number
122         1               0*10+1 = 1
12          2               1*10+2 = 12
This is middle as 12==12 -> Palindrome


12321
rem x       last digit      reversed number
1232        1               0*10+1 = 1
123         2               1*10+2 = 12
12          3               12*10+3 = 123
This is middle as 123>12 -> 123//10==12 -> Palindrome


12345
rem x       last digit      reversed number
1234        5               0*10+5 = 5
123         4               5*10+4 = 54
12          3               54*10+3 = 543
This is middle as 543>12 -> 543//10!=12 -> Not Palindrome

'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x==0: return True    # Case : Integer is 0
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