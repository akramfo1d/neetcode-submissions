class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=defaultdict(int)
        freq=[[]for i in range(len(nums)+1)]

        for i in nums:
            result[i]+=1

        for z,v in result.items():
            freq[v].append(z)
        res=[]

        for i in range(len(freq)-1,0,-1):
            
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res


        
        
        
        