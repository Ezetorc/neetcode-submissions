class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        result = []

        for value in strs:
            key = ''.join(sorted(value))

            if key in hashmap:
                hashmap[key].append(value)
            else:
                hashmap[key] = [value]
        
        for value in hashmap.values():
            result.append(value)

        return result