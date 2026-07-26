import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        result = []

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        sorted_items = heapq.nlargest(k, seen.items(), key=lambda item: item[1])

        for num, _ in sorted_items:
            result.append(num)
        
        return result

        



            