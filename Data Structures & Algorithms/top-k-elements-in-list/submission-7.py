class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        result = []

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        for num, frequency in sorted(seen.items(), key=lambda item: item[1], reverse=True):
            result.append(num)
        
        return result[:k]

        



            