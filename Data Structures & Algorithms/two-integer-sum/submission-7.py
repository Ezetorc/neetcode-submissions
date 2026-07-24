class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [5, 5] = 10  > [0, 1]
        # [4, 5, 6] = 10  > [0, 2]

        for i, v in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []