class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        remainder = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num

            rem = prefix_sum % k

            if rem in remainder:
                if i - remainder[rem] >= 2:
                    return True
            else:
                remainder[rem] = i

        return False