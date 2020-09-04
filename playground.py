from collections import *
from itertools import *
from random import *
import sys
import time
from typing import List

class Solution:
    def minOverallAwkwardness(self, arr: List) -> int:
        DEBUG = 0
        arr.sort()
        def is_good(x: int) -> bool:
            q = deque()
            for a in arr:
                if not q:
                    q.append(a)
                    continue
                left_dif = a - q[0]
                right_dif = a - q[-1]
                if max(left_dif, right_dif) <= x:
                    if left_dif > right_dif:
                        q.appendleft(a)
                    else:
                        q.append(a)
                else:
                    if DEBUG: print(f"{x} is not good")
                    return False
            if DEBUG: print(f"{x} is good, q {q}")
            return True

        min_a, max_a = arr[0], arr[-1]
        l, h = arr[1] - arr[0], max_a - min_a
        if DEBUG: print(f"l {l}, h {h}")
        while l < h:
            m = (l + h) // 2
            if is_good(m):
                h = m
            else:
                l = m + 1
        return l

def generate_random_list(size, length, with_dup = True):
    if not with_dup:
        return sample(range(1, size), length)
    l1 = sample(range(1, size), length // 2)
    l2 = sample(range(1, size), (length + 1) // 2)
    return l1 + l2

if __name__ == "__main__":
    solution = Solution()
    start = time.time()
    for _ in range(10):
        l = generate_random_list(50, 7)
        print(f"testing with {l}")
        my_ans = solution.minOverallAwkwardness(l)
        brute_ans = max(l)
        for x in permutations(l):
            check = list(x) + [x[0]]
            brute_ans = min(brute_ans, max(abs(a - b) for a, b in zip(check, check[1:])))
        assert brute_ans == my_ans
        print(f"ans is {my_ans}")
    end = time.time()
    print("time: ", end - start)