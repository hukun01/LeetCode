# 395. Longest Substring with At Least K Repeating Characters
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        Sliding window.
        The key in this problem is to identify WHEN to shrink the window size.
        Unlike other sliding window problems where we have constraint to not
        exceed certain limit, and we can start shrinking the window once we
        exceed the limit. In this problem, there's no such limit, so there is
        no trigger for shrinking. We need to put some limit on our own to guide
        the sliding window on when to shrink.

        Have a helper method to find the longest substring length with exactly
        n unique chars, each of which appears at least k times. In this method,
        we can use sliding window as we know when there are more than n unique
        chars in the window, it's time to shrink the left side. We just need to
        also keep track of number with at least k frequency.

        As we know there's up to len(set(s)) unique chars, we can try each
        unique count with the helper method.

        Time: O(cn) where n is the length of the string s, c is the total
        number of unique chars in the problem, in this case it's up to 26.
        Space: O(c).
        Follow-up: How to handle arbitrary char set where there can be many
        more than 26 chars?
        In this case, c can be huge, we need to shrink the upper bound of c.
        The upper bound of feasible unique count is when the whole string s
        is good, in which each char has at least k times.
        Hence, the upper bound is the number of chars that appear at least k.
        In this case, c <= n / k.
        Note that also upper bound <= 26 as Counter() only covers unique chars.
        '''
        def longest_substr_with_n_unique(num_unique_target):
            freqs = Counter()
            num_unique = num_at_least_k = begin = end = ans = 0
            while end < len(s):
                char = s[end]
                if freqs[char] == 0:
                    num_unique += 1
                freqs[char] += 1
                if freqs[char] == k:
                    num_at_least_k += 1
                end += 1

                while num_unique > num_unique_target:
                    char = s[begin]
                    if freqs[char] == k:
                        num_at_least_k -= 1
                    freqs[char] -= 1
                    if freqs[char] == 0:
                        num_unique -= 1
                    begin += 1

                if num_unique == num_at_least_k:
                    ans = max(ans, end - begin)
            return ans

        upper_bound = sum(v >= k for v in Counter(s).values())
        ans = 0
        for num_unique_target in range(1, upper_bound + 1):
            ans = max(ans, longest_substr_with_n_unique(num_unique_target))
        return ans