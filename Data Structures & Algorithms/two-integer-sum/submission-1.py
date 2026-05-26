class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for idx, num in enumerate(nums):
            if num in memo:
                return [memo[num], idx]
            memo[target - num] = idx