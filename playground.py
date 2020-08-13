import collections
import itertools
import random
import sys
import time
from typing import List

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for c in [num + 1, num + 2]:
            x = int(c ** 0.5)
            if x ** 2 == c:
                return [x, x]
        
        def get(target):
            ans = [-1, -1]
            delta = float('inf')
            for i in range(int(target ** 0.5), 0, -1):
                if target % i == 0:
                    diff = abs(i - target // i)
                    if diff < delta:
                        ans = [i, target // i]
                        delta = diff

            return ans
        return min(get(num + 1), get(num + 2), key=lambda x: abs(x[1] - x[0]))

if __name__ == "__main__":
    solution = Solution()
    start = time.time()
    print(solution.closestDivisors(129045830))
    end = time.time()
    print("time: ", end - start)