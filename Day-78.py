2295. Replace Elements in an Array.py
class Solution:
    def arrayChange(self, nums, operations):
        
        index = {}

        # Store value -> index
        for i in range(len(nums)):
            index[nums[i]] = i

        # Perform operations
        for old, new in operations:
            pos = index[old]

            nums[pos] = new

            # Update mapping
            index[new] = pos
            del index[old]

        return nums
