1460. Make Two Arrays Equal by Reversing Subarrays.py
class Solution:
    def canBeEqual(self, target, arr):
        target.sort()
        arr.sort()
        return target == arr
