class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        val=1
        max=1
        if nums==[]:
            return 0
        for i in range(0,len(nums)-1):
            if nums[i+1]-nums[i]==1:
                max+=1
            elif nums[i+1]-nums[i]==0:
                continue
            else:
                if val <= max :
                    val=max
                max=1
                
        if val < max:
            val = max

        return val