class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        counts = [0] * 26

        for s_char in s:
            counts[ord(s_char) - 97] += 1
        
        for t_char in t:
            counts[ord(t_char) - 97] -= 1
        
        return not any(counts)
