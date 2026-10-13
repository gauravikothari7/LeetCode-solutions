
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums = sorted(x * x for x in nums)
        mid = len(nums) // 2
        return sum(nums[mid:]) - sum(nums[:mid])