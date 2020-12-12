# 698. Partition to K Equal Sum Subsets
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        '''
        1/2 DFS with backtracking.
        The key difference between finding a subset vs finding k subsets,
        is that in the latter, we keep track of count, and only return true
        when count is 0. We also need to ensure the total sum is k * target.

        Another key is to backtrack, because one valid set may cause another
        one invalid, so we need to be able to revert and try other paths.

        Yet another key is to break early when one bucket isn't feasible to
        hold any value.

        Time: O(k! k^(n-k)) where n is len(nums), we call (k!) times of dfs(),
        and each dfs() takes k^(n-k) steps for each bucket.
        Space: O(n)
        '''
        target, remaining = divmod(sum(nums), k)
        if remaining != 0:
            return False
        buckets = [0] * k
        nums.sort(reverse=True)
        def dfs(i):
            if i == len(nums):
                return True
            for b_idx in range(k):
                buckets[b_idx] += nums[i]
                if buckets[b_idx] <= target and dfs(i + 1):
                    return True
                buckets[b_idx] -= nums[i]
                if buckets[b_idx] == 0:
                    break
            return False
        return dfs(0)
        '''
        2/2 Bitmask DP.

        Each number has two states, used or not, so there are 2^n total states.
        Let f[used] be the answer with numbers used marked as 1.
        Let total[used] be the sum of used numbers. Then we have
        f[used_add_i] = f[used] & ((total[used] % target) + nums[i] <= target)
        Note that we need mod total[used] by target.

        And the answer is f[last_used] where last_used has all bits set to 1.

        Time: O(n 2^n)
        Space: O(2^n)
        '''
        target, remaining = divmod(sum(nums), k)
        if remaining != 0:
            return False

        total_states = 1 << len(nums)
        f = [False] * total_states
        f[0] = True
        total = [0] * total_states

        nums.sort()
        for state in range(total_states):
            if not f[state]:
                continue
            for i, a in enumerate(nums):
                if a + (total[state] % target) > target:
                    break
                next_state = state | (1 << i)
                if state != next_state and not f[next_state]:
                    f[next_state] = True
                    total[next_state] = total[state] + a
        return f[-1]