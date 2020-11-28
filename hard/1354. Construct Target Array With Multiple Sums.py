# 1354. Construct Target Array With Multiple Sums
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        '''
        Math.
        From initial array to target there can be many branches, it seems no
        way to reach target deterministically, so we try working backwards.
        From target to initial array, in the last step, only the biggest num
        must be updated, otherwise, it contradicts with the fact that all
        numbers are positive.

        The biggest in target consist of prev_max and other_sum, where prev_max
        is the previous max number, and other_sum is the sum of other numbers
        except prev_max, and prev_max + other_sum = previous sum = biggest.
        Thus, we have 2 formulas:
            other_sum = total - biggest     (1)
            prev_max = biggest - other_sum  (2)
        prev_max gives us one step backward from target to initial array. Keep
        doing this until the biggest == 1, then it is possible. If prev_max
        becomes 0 or it's not decreasing from biggest, then it's impossible.
        Note that we need to do modulus in formula (2), as it could be that
        biggest >> other_sum, like [1,10000].

        Similar to 780. Reaching Points.
        '''
        if len(target) == 1:
            return target == [1]
        total = sum(target)
        target = [-a for a in target]
        heapify(target)
        while (biggest := -target[0]) > 1:
            other_sum = total - biggest

            # Only happen when n = 2, like [1,1000]
            if other_sum == 1:
                return True

            prev_max = biggest % other_sum
            if prev_max == 0 or prev_max == biggest:
                return False
            heapq.heapreplace(target, -prev_max)
            total = other_sum + prev_max
        return True