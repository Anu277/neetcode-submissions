class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index in range(0, len(nums) - 2):

            if index > 0 and nums[index] == nums[index - 1]:
                continue

            l = index + 1
            r = len(nums) - 1

            while l < r:

                if nums[l] + nums[r] + nums[index] > 0:
                    r -= 1

                elif nums[l] + nums[r] + nums[index] < 0:
                    l += 1

                else:
                    res.append([nums[index], nums[l], nums[r]])

                    l += 1
                    # r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # while l < r and nums[r] == nums[r + 1]:
                    #     r -= 1

        return res