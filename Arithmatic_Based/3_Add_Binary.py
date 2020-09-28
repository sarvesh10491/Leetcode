class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = ""
        i,j = len(a)-1,len(b)-1
        summ,car = 0,0
        
        while i>-1 and j>-1:
            summ = int(a[i])+int(b[j])+car

            if summ == 2:
                ans += "0"
                car = 1
            elif summ == 3:
                ans += "1"
                car = 1
            else:
                ans += str(summ)
                car = 0
            i -= 1
            j -= 1
        
        
        while i>-1:
            summ = int(a[i])+car
            
            if summ == 2:
                ans += "0"
                car = 1
            elif summ < 2:
                ans += str(summ)
                car = 0
            i -= 1
        
        
        while j>-1:
            summ = int(b[j])+car
            if summ == 2:
                ans += "0"
                car = 1
            elif summ < 2:
                ans += str(summ)
                car = 0
            j -= 1
        
        if car:
            ans += "1"
        
        return str(ans[::-1])