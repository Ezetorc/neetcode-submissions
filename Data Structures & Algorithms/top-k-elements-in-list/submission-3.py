class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        result = []

        for num in nums:
            if num in seen:
                seen[num] = [seen[num][0] + 1, num]
            else:
                seen[num] = [1, num]
        
        for frequency, key in sorted(
            seen.values(), 
        ):
            result.insert(0, seen[key][1])
        
        return result[:k]



            