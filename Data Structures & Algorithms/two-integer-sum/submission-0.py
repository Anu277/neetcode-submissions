class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i,v in enumerate(nums):
            rem=target-v
            if rem in s:
                return [s[rem],i]
            s[v]=i