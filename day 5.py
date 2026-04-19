28.find the index of first occurance in the string
class Solution:
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)
        
        for i in range(n - m + 1):
            j = 0
            
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            
            if j == m:
                return i
        
        return -1
35.search insert position
class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left