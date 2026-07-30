class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for number in numbers:
            if number - 1 not in numbers:
                length = 0

                while number + length in numbers:
                    length += 1
                
                longest = max(length, longest)
        
        return longest