class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
                max_ones = max(max_ones, cnt)
            else:
                cnt = 0
        return max_ones