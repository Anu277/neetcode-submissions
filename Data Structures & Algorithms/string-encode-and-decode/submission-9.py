class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        r=""
        
        for s in strs:
            result+=str(len(s))
            result+=","
            r+=s
        result+="#"
        result+=r
        return result

    def decode(self, s: str) -> List[str]:
        result=[]
        l=[]
        i=0
        while(s[i]!="#"):
            j=i
            while(s[j]!=","):
                j+=1
            l.append(int(s[i:j]))
            i=j+1
        i+=1
        for k in l:
            result.append(s[i:i+k])
            i=i+k
        return result
            


