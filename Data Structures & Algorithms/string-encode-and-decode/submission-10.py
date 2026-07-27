class Solution:
    def encode(self, strs: list[str]) -> str:
        result = []

        for word in strs:
            fragment = [str(len(word)), "#", word]
            result.extend(fragment)

        return "".join(result)

    def decode(self, s: str) -> list[str]:
        result = []
        index = 0

        while index < len(s):
            start = index

            while index < len(s) and s[index] != "#":
                index += 1
            
            word_length = int(s[start:index])

            word_start = index + 1
            word_end = word_start + word_length

            word = s[word_start:word_end]
            index = word_end
          
            result.append(word)

        return result