class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    output = 0
    left = 0
    chars = {}

    for right in range(len(s)):
      rightChar = s[right]
      chars[rightChar] = chars.get(rightChar, 0) + 1
      windowSize = right - left + 1
      frequency = max(chars.values())
      replacements = windowSize - frequency

      while replacements > k:
        char_l = s[left]
        chars[char_l] -= 1

        left += 1
        windowSize = right - left + 1
        frequency = max(chars.values())
        replacements = windowSize - frequency

      output = max(output, right - left + 1)

    return output