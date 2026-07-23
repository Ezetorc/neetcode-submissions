class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        counts = [0] * 26
        a_ascii_code = ord("a")

        for index in range(len(s)):
            counts[ord(s[index]) - a_ascii_code] += 1
            counts[ord(t[index]) - a_ascii_code] -= 1

        return not any(counts)
