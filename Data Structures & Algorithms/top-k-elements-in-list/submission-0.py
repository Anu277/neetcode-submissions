class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq=Counter(nums)
        top=freq.most_common(k)
        result=[]
        for num,rep in top:
            result.append(num)

        return result
