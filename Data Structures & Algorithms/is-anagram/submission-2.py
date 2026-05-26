from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_counter, t_counter = Counter(s), Counter(t)
        if len(s_counter) != len(t_counter): return False

        for key in s_counter.keys():
            if s_counter[key] != t_counter[key]: return False
        
        return True