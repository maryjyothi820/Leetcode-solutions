912._sort_an_array
class Solution:
    def sortArray(self, nums):
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums, left, right):
        if left >= right:
            return

        mid = (left + right) // 2

        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        temp = []
        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= right:
            temp.append(nums[j])
            j += 1

        for k in range(len(temp)):
            nums[left + k] = temp[k]
3446.sort_matrix_by_daigonals
class Solution:
    def sortMatrix(self, grid):
        n = len(grid)
        diag = {}

        # Step 1: collect diagonals
        for i in range(n):
            for j in range(n):
                key = i - j
                if key not in diag:
                    diag[key] = []
                diag[key].append(grid[i][j])

        # Step 2: sort each diagonal
        for key in diag:
            if key >= 0:
                # bottom-left triangle → non-increasing
                diag[key].sort(reverse=True)
            else:
                # top-right triangle → non-decreasing
                diag[key].sort()

        # Step 3: put back values
        for i in range(n):
            for j in range(n):
                key = i - j
                grid[i][j] = diag[key].pop(0)

        return grid