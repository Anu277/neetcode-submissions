class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        forward = []
        stored = 1

        for i in nums:
            forward.append(stored)
            stored *= i

        backward = []
        stored = 1

        for i in reversed(nums):
            backward.append(stored)
            stored *= i

        backward.reverse()
        tot=[]
        for i in range(len(forward)):
            tot.append(forward[i]*backward[i])
        return tot
