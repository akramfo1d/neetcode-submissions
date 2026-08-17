class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0
        prefixsum = {0: 1}

        for i in nums:
            currsum += i
            diff = currsum - k

            res += prefixsum.get(diff, 0)

            prefixsum[currsum] = prefixsum.get(currsum, 0) + 1

        return res