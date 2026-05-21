class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l <= r:
            cur = (l + r) // 2
            time_taken = sum(pile // cur + (1 if pile % cur != 0 else 0) for pile in piles)
            if time_taken <= h:
                k = cur
                r = cur - 1
            else:
                l = cur + 1
        return k