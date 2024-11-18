class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # 計算當前面積
            current_area = min(height[left], height[right]) * (right - left)
            # 更新最大面積
            max_area = max(max_area, current_area)

            # 移動指針
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
