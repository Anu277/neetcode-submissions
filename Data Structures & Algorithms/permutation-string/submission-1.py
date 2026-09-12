class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        s2l=len(s2)
        s1l=len(s1)

        s1c=Counter(s1)
        i=0
        s={}
        while(i<s2l):
            s=Counter(s2[i:i+s1l])
            if s1c==s:
                return True
            i+=1
        return False

