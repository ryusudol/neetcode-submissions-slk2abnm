class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = []
        largest_seen = -1
        for i in range(len(arr) - 1, -1, -1):
            stack.append(largest_seen)
            largest_seen = max(largest_seen, arr[i])
        return stack[::-1]