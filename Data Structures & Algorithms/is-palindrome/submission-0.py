class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(filter(str.isalnum, s)).lower()

        for index, char in enumerate(string):
            if char != string[len(string) - (index + 1)]:
                return False
        
        return True