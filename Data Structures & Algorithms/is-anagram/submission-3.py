class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        counts = [0] * 26
        a_ascii_code = ord("a")

        for s_char, t_char in zip(s, t):
            counts[ord(s_char) - a_ascii_code] += 1
            counts[ord(t_char) - a_ascii_code] -= 1

        return not any(counts)
