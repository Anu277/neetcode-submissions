class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        left = 0
        right = 0
        left_max = height[0]
        water = 0

        while right < n:
            if height[right] >= left_max:
                # Found a right boundary
                for i in range(left + 1, right):
                    water += left_max - height[i]

                left = right
                left_max = height[left]

            right += 1

        right = n - 1
        right_max = height[right]

        for i in range(n - 2, left - 1, -1):
            if height[i] >= right_max:
                right_max = height[i]
            else:
                water += right_max - height[i]

        return water