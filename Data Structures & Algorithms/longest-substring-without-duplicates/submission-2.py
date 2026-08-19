class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count=defaultdict(int)
        maxcount=0

        l=0

        for r in range(len(s)):
            count[s[r]]+=1

            while count[s[r]]>1:
                count[s[l]]-=1
                l+=1
            maxcount=max(maxcount,r-l+1)

            r+=1
        return maxcount
            

