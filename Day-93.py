2384. Largest Palindromic Number.py
from collections import Counter
class Solution:
    def largestPalindromic(self, num):
        count = Counter(num)
        left = []
        for digit in range(9, -1, -1):
            d = str(digit)
            left.append(d * (count[d] // 2))
        left = "".join(left)
        left = left.lstrip("0")
        middle = ""
        for digit in range(9, -1, -1):
            d = str(digit)
            if count[d] % 2 == 1:
                middle = d
                break
        if left == "":
            if middle:
                return middle
            return "0"
        return left + middle + left[::-1]
