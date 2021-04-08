# 1815. Maximum Number of Groups Getting Fresh Donuts
class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        '''
        Memoized DFS.

        We only need to consider the group % batchSize rather than the actual
        group values, because only the remaining number determines whether the
        current batch fits.

        Obviously the groups that can fit into the batch size would be
        satisfied (remainder = 0). We can count them in first.

        Also, for any group pair that complement each other, we can only
        satisfy one group.

        For the rest of the groups, we do a brute force memoized DFS to find
        the best assignments. This is feasible because the batchSize <= 9 and
        len(groups) <= 30.

        Time: O(k * 2^k) where k is batch size. Note that although there can be
              at most n = len(groups) element in the later 'groups' tuple,
              there is only 2^k different tuples, because the elements are
              oganized consecutively. For example, from (1,1,2,2), if we remove
              a '2', we get (1,1,2), regardless of which '2' is removed.
        Space: O(k * 2^k)
        '''
        n = len(groups)

        groups = [i % batchSize for i in groups if i % batchSize]

        satisfied = n - len(groups)

        matching = Counter()
        for group in groups:
            if matching[batchSize - group] > 0:
                matching[batchSize - group] -= 1
                satisfied += 1
            else:
                matching[group] += 1

        groups = []
        for group, count in matching.items():
            groups += [group] * count

        @cache
        def dfs(cur_group_size: int, groups: tuple) -> int:
            if not groups:
                return 0

            ans = 0
            for i in range(len(groups)):
                next_groups = groups[0: i] + groups[i + 1:]
                next_group_size = (cur_group_size + groups[i]) % batchSize
                ans = max(ans, dfs(next_group_size, next_groups))

            return ans + int(cur_group_size == 0)

        return dfs(0, tuple(groups)) + satisfied