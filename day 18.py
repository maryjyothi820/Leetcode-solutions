2.add two numbers
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        temp = dummy
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            total = carry

            if l1 != None:
                total = total + l1.val
                l1 = l1.next

            if l2 != None:
                total = total + l2.val
                l2 = l2.next

            carry = total // 10
            digit = total % 10

            temp.next = ListNode(digit)
            temp = temp.next

        return dummy.next
11.container with most water 
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            h = height[left]
            if height[right] < h:
                h = height[right]

            width = right - left
            area = h * width

            if area > max_water:
                max_water = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water