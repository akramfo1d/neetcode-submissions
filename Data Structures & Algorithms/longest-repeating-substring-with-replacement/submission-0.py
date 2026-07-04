class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap=defaultdict(int)
        res=0
        l=0
        for r in range(len(s)):
            hashmap[s[r]]+=1
            while (r-l+1)-max(hashmap.values())>k:
                hashmap[s[l]]-=1
                l+=1
            res=max(res,r-l+1)


        return res



        
        