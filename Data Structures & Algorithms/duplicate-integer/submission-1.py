class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_repeated_nums = set()

        for num in nums:
            if num in non_repeated_nums:
                return True
            
            non_repeated_nums.add(num)
       
        return False

        