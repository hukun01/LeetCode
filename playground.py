import collections
import itertools
import random
import sys
import time
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        maps = collections.defaultdict(list)
        [maps[a].append(i) for i, a in enumerate(arr)]
 
        begins = set([0])
        ends = set([len(arr) - 1])
        visitedIdx = set([-1, len(arr)])
        for steps in range(len(arr)):
            if len(begins) > len(ends):
                begins, ends = ends, begins
            nextLevels = set()
            for b in begins:
                if b in ends:
                    return steps
                if b in visitedIdx:
                    continue
                visitedIdx.add(b)
                nextLevels.update([b - 1, b + 1] + maps[arr[b]])
                maps.pop(arr[b])
            begins = nextLevels
    def minJumps2(self, arr: List[int]) -> int:
        maps = collections.defaultdict(list)
        [maps[a].append(i) for i, a in enumerate(arr)]
        
        visitedIdx = set([-1, len(arr)])
        q = collections.deque([(0, 0)])
        while q:
            step, pos = q.popleft()
            if pos == len(arr) - 1:
                return step
            for p in [pos - 1, pos + 1] + maps[arr[pos]]:
                if p not in visitedIdx:
                    visitedIdx.add(p)
                    q.append((step + 1, p))
            maps.pop(arr[pos])

if __name__ == "__main__":
    solution = Solution()
    ls = []
    for _ in range(400):
        l = list(range(10000))
        random.shuffle(l)
        ls.append(l)
    for func in [solution.minJumps, solution.minJumps2]:
        start = time.time()
        for l in ls:
            func(l)
        end = time.time()
        print("time: ", end - start)