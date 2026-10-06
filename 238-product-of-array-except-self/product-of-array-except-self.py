class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = [1] * n
        right = [1] * n
        answer = [0] * n

        # build left: product of numbers to the left of each position
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # build right: product of numbers to the right of each position
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # multiply box by box
        for i in range(n):
            answer[i] = left[i] * right[i]

        return answer