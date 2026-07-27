class Solution:
    def encode(self, strs: list[str]) -> str:
        result = []

        for word in strs:
            result.append(f"{len(word)}#{word}")

        return "".join(result)

    def decode(self, s: str) -> list[str]:
        result = []
        index = 0

        while index < len(s):
            length_start = index

            while s[index] != "#":
                index += 1
            
            word_length = int(s[length_start:index])

            word_start = index + 1
            word_end = word_start + word_length
          
            result.append(s[word_start:word_end])
            index = word_end

        return result