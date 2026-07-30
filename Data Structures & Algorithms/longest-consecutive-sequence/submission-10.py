class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        numbers = set(nums)
        results = []

        for number in numbers:
            if number - 1 not in numbers:
                length = 1

                while True:
                    if number + length in numbers:
                        length += 1
                    else:
                        break
                
                results.append(length)
        
        return sorted(results, reverse=True)[0]







                