58.lenght of last word
class Solution:
    def lengthOfLastWord(self, s):
        length = 0
        i = len(s) - 1
        
        # skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # count characters of last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length
66.plus one
class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        # start from last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        # if all digits were 9
        return [1] + digits
67.add binary
class Solution:
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ""
        
        while i >= 0 or j >= 0 or carry:
            sum_val = carry
            
            if i >= 0:
                sum_val += int(a[i])
                i -= 1
            
            if j >= 0:
                sum_val += int(b[j])
                j -= 1
            
            result = str(sum_val % 2) + result
            carry = sum_val // 2
        
        return result