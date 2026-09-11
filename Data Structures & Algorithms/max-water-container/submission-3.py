class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ar=0
        l=0
        r=len(heights)-1
        
        while(r>l):

            ar=max(ar,(r-l)*min(heights[r],heights[l]))
            print(ar)
            
            if heights[l]<=heights[r]:
                l=l+1
            else:
                r=r-1

        return ar
