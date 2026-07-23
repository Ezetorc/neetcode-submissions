class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        for index, s_char in enumerate(s):
            if s_char in t:
                s = s[1:]
                t = t.replace(s_char, "", 1)
            else:
                return False
        
        return True
