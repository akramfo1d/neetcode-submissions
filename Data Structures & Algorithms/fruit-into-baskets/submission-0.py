from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(fruits)):
            counter[fruits[r]] += 1

            # Keep only 2 types of fruits in the window
            while len(counter) > 2:
                counter[fruits[l]] -= 1

                if counter[fruits[l]] == 0:
                    del counter[fruits[l]]

                l += 1

            # Update maximum valid window
            res = max(res, r - l + 1)

        return res