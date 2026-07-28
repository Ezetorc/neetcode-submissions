class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i, num1 in enumerate(nums):
            subresult = 1

            for j, num2 in enumerate(nums):
                if i == j: continue

                subresult *= num2
            
            result.append(subresult)
        
        return result