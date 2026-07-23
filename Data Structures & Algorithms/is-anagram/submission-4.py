class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        char_counts = [0] * 26
        base = ord("a")

        for s_char, t_char in zip(s, t):
            s_index = ord(s_char) - base
            t_index = ord(t_char) - base
            
            char_counts[s_index] += 1
            char_counts[t_index] -= 1

        return not any(char_counts)
