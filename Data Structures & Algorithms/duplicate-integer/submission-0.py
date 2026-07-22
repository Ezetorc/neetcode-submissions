class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_repeated_nums = []

        for num in nums:
            if not num in non_repeated_nums:
                non_repeated_nums.append(num)
        
        return len(nums) != len(non_repeated_nums)

        