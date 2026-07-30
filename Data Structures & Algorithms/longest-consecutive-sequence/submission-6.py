class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0: return 0
        
        numbers = sorted(set(nums))
        results = []
        current = 0
        
        print(" Numbers: " + str(numbers))

        while current < len(numbers):
          start = current
          
          while (
            current + 1 < len(numbers) and 
            numbers[current + 1] == numbers[current] + 1
          ):
            current += 1
          
          results.append(numbers[start:current + 1])

          current += 1
        
        return len(sorted(results, key=len, reverse=True)[0])