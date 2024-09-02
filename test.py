class Solution:
    def longestCommonPrefix(self, v: list[str]) -> str:
        ans=""
        v=sorted(v)
        print(v)
        first=v[0]
        last=v[-1]
        print(first)
        print(last)
        print(min(len(first),len(last)))
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
    
r = Solution()
strs = ["flawer","floh","flaigt"]

print(r.longestCommonPrefix(strs))