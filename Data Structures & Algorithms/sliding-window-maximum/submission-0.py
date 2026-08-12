from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # stores indices
        res = []

        for r in range(len(nums)):

            # Remove indices that are outside the current window
            if dq and dq[0] <= r - k:
                dq.popleft()

            # Maintain decreasing order in deque
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)

            # Start adding results when the first window is complete
            if r >= k - 1:
                res.append(nums[dq[0]])

        return res