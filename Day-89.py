817. Linked List Components.py
class Solution:
    def numComponents(self, head, nums):
        nums_set = set(nums)
        count = 0

        while head:
            if head.val in nums_set and (head.next is None or head.next.val not in nums_set):
                count += 1
            head = head.next

        return count
        
