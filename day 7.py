69.sqrt(x)
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 1, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right
70.climbing stairs
class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        first, second = 1, 2
        
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        
        return second
83.remove duplicates from sorted list
class Solution:
    def deleteDuplicates(self, head):
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
