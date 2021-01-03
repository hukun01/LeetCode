# 1675. Minimize Deviation in Array
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        '''
        1/2 Priority queue + sliding window.
        For any number, either of 2 directions can be taken, so we enumerate
        all possible numbers, and find the smallest number range that covers
        all positions.
            1. For an even number a, the possible numbers are [a, a//2, ...
            until we reach an odd number];
            2. For an odd number a, the possible numbers are [a, a*2].

        Time: O(k log(m) + k log(m) log(k)) where m is the largest number that
        is also a power of 2, k is len(nums). First part is building the
        possible array, second part is to find the smallest range.
        Space: O(nk)

        Similar to 632. Smallest Range Covering Elements from K Lists.
        '''
        possible = [[] for _ in range(len(nums))]
        for i, a in enumerate(nums):
            possible[i].append(a)
            if a % 2 == 0:
                while a % 2 == 0:
                    a //= 2
                    possible[i].append(a)
                possible[i] = possible[i][::-1]
            else:
                possible[i].append(a * 2)
        ans = self.smallestRange(possible)
        return ans[1] - ans[0]

    def smallestRange(self, num_lists: List[List[int]]) -> List[int]:
        starts = [(a[0], i, 0) for i, a in enumerate(num_lists)]
        heapify(starts)
        ans = [1, 1e9]
        end = max(a[0] for a in num_lists)
        while starts:
            start, list_idx, start_i = heappop(starts)
            if end - start < ans[1] - ans[0]:
                ans = [start, end]
            if start_i + 1 == len(num_lists[list_idx]):
                break
            start = num_lists[list_idx][start_i + 1]
            end = max(end, start)
            heappush(starts, (start, list_idx, start_i + 1))
        return ans
    '''
    2/2 Priority queue
    Note that if a number is even, we can't increase it; If a number is odd,
    we can't decrease it. As we try to minimize (max - min), we either decrease
    max, or increase min. To reduce the search space, we can increase all odd
    numbers by doubling them, then later we just need to check if we should
    decrease them.
    Maintain a max-heap with possible max numbers, if seeing an even number, we 
    just add it; if seeing an odd number a, add a*2. A max-heap helps tracking
    new values added as the max numbers.
    Also find the cur_min in the max-heap.
    Now we can't further increase any max numbers, just try decreasing them,
    and compare them with cur_min to get the min deviation.
    Go over all possible max numbers in the max-heap, until a max number
    cannot be further decreased (by being divided by 2).
    If a max number can be divided by 2, divide it, add it back to max-heap,
    and also update cur_min.

    Time: O(k log(n)) where n is len(nums), k is n * log(m), where m is the
          largest number that is also a power of 2 (so it can be divided by 2
          until becoming 1).
    Space: O(n)
    '''
    possible_maxs = [-a * 2 if a % 2 == 1 else -a for a in nums]
    cur_min = -max(possible_maxs)
    heapify(possible_maxs)
    ans = inf
    while possible_maxs:
        cur_max = -heappop(possible_maxs)
        ans = min(ans, abs(cur_max - cur_min))
        if cur_max % 2 == 0:
            cur_max //= 2
            cur_min = min(cur_min, cur_max)
            heappush(possible_maxs, -cur_max)
        else:
            break
    return ans