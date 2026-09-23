class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        maxi=max(piles)
        left=1
        right=maxi
        while(left<=right):
            k=(left+right)//2
            hours=0
            for i in piles:
                j=(i+k-1)//k
                hours+=j
            if hours<=h:
                right=k-1
            else :
                left=k+1

        return left
                