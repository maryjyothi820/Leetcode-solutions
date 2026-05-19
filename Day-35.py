189.Rotate_array.py
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        
        nums[:] = nums[-k:] + nums[:-k]