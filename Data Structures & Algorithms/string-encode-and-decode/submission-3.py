class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        r=""
        
        for s in strs:
            result+=str(len(s))
            result+=","
            r+=s
        #l=len(result)
       # result=result[0:l-1]
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
        print(l)
        i+=1
        c=0
        for k in l:
            print(s[i:i+k])
            result.append(s[i:i+k])
            i=i+k
        return result
            


