class Solution:
    def encode(self, strs: list[str]) -> str:
        result = []

        for word in strs:
            result.extend([str(len(word)), "#", word])

        return "".join(result)

    def decode(self, s: str) -> list[str]:
        result = []
        index = 0

        while index < len(s):
            start = index

            while index < len(s) and s[index] != "#":
                index += 1
            
            word_length = int(s[start:index])
            word = s[index + 1:index + word_length + 1]

            index += word_length + 1
          
            result.append(word)

        return result