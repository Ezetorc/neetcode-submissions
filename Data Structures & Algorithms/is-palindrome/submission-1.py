class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = ''.join(filter(str.isalnum, s)).lower()

        return output == output[::-1]