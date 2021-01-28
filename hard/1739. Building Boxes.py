# 1739. Building Boxes
class Solution:
    def minimumBoxes(self, n: int) -> int:
        '''
        Math + greedy.
        Intuitively, (don't know how to prove), we want to build a complete
        triagular pile like the example shows. This uses the min number of
        boxes touching the floor.
        We need ∑(1, level) cubes to build a complete triangular pile for each
        level. See picture in https://leetcode.com/problems/building-boxes/discuss/1032016/C%2B%2B-Python-3-variables-solution-with-drawing-explanation.
        Let cubes[0] be the top level cubes, and cubes[-1] be the bottom level
        cubes. Use cubes to build total_cubes. If total_cubes[-1] == n, then
        we have a perfect triangular pile, we can return cubes[-1].
        Otherwise, the last level isn't full, we need to add it via smaller
        triangular pile (see picture in above link)

        Time: O(n^(1/3))
        Space: O(n^(1/3))
        '''
        cubes = [1] # cubes at the top level
        total_cubes = [1]
        while total_cubes[-1] < n:
            cubes.append(cubes[-1] + len(cubes) + 1)
            total_cubes.append(total_cubes[-1] + cubes[-1])

        if total_cubes[-1] == n: return cubes[-1]

        ans = cubes[-2]
        count = 1
        for i in range(1, len(cubes) + 1):
            count += i
            ans += 1
            if count > n - total_cubes[-2]: break

        return ans