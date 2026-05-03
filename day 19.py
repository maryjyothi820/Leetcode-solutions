168.excel sheet column title
class Solution:
    def convertToTitle(self, columnNumber):
        result = ""

        while columnNumber > 0:
            columnNumber = columnNumber - 1
            remainder = columnNumber % 26

            char = chr(65 + remainder)
            result = char + result

            columnNumber = columnNumber // 26

        return result
169.majority element
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count = count + 1
            else:
                count = count - 1

        return candidate