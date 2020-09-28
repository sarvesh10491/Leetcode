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
        
        # Loop to sum each position digit wise until both strings have digits
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
        

        # Loop to sum remaining digits in longer string until carry is 1
        while i>-1:
            summ = int(a[i])+car
            
            if summ == 2:
                ans += "0"
                car = 1
            elif summ < 2:
                ans += str(summ)
                ans += a[:i][::-1]
                car = 0
                break
            i -= 1
        
        
        while j>-1:
            summ = int(b[j])+car
            if summ == 2:
                ans += "0"
                car = 1
            elif summ < 2:
                ans += str(summ)
                ans += b[:j][::-1]
                car = 0
                break
            j -= 1
        
        # Add 1 if there is trailing carry in end
        if car:
            ans += "1"
        
        return str(ans[::-1])