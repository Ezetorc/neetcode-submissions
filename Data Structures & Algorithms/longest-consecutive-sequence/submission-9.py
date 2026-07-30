class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        numbers = set(nums)
        results = []

        for number in numbers:
            if number - 1 not in numbers:
                sublist = []
                lastNumber = number + 1

                while True:
                    if lastNumber in numbers:
                        sublist.append(lastNumber)
                        lastNumber += 1
                    else:
                        break
                
                results.append(sublist)
        
        return len(sorted(results, reverse=True, key=len)[0]) + 1







                