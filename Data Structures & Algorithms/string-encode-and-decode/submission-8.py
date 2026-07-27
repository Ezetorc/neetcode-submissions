class Solution:
    def encode(self, strs: list[str]) -> str:
        result = ""

        for word in strs:
            result += f"{len(word)}#{word}"

        return result

    def decode(self, s: str) -> list[str]:
        result = []
        length = len(s)
        index = 0

        while index < length:
            start = index

            while index < length and s[index] != "#":
                index += 1
            
            word_length = int(s[start:index])
            word = s[index + 1:index + word_length + 1]

            index += word_length + 1
          
            result.append(word)

        return result