217.contains duplicates
class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
219.contains duplicates 2
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}
        
        for i in range(len(nums)):
            if nums[i] in index_map and i - index_map[nums[i]] <= k:
                return True
            
            index_map[nums[i]] = i
        
        return False 