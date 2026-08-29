class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # x=set(nums)
        # if len(nums)==len(x):
            # return False
        return len(set(nums))!=len(nums)