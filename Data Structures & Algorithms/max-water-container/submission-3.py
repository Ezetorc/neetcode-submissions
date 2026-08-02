class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            leftHeight = heights[left]
            rightHeight = heights[right]

            width = right - left
            height = min(leftHeight, rightHeight)
            result = max(result, width * height)

            if leftHeight < rightHeight:
                left += 1
            else:
                right -= 1

        return result