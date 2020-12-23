# 395. Longest Substring with At Least K Repeating Characters
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        1/3 Divide and conquer.
        Divide: divide the input by the first char whose count < k, or return
            the whole length.
        Conquer: combine the result from sub problems, to take the max length.

        Time: O(n^2) where n is the length of the string s
        Space: O(n) for stack
        '''
        def longest_until(start, end):
            count = Counter(s[start: end])
            for mid in range(start, end):
                if count[s[mid]] >= k:
                    continue
                mid_next = mid + 1
                while mid_next < end and count[s[mid_next]] < k:
                    mid_next += 1
                return max(longest_until(start, mid), longest_until(mid_next, end))
            return end - start
        return longest_until(0, len(s))
        '''
        2/3 Sliding window.
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

        Time: O(cn) where c is the total number of unique chars in the problem,
              in this case it's up to 26.
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
        '''
        2/3 A simple implementation to find longest substr with x unique chars.

        Time: O(n U) where n is len(s), U is total number of unique chars in s.
        Space: O(U).
        '''
        def longest_substr_with_n_unique(num_unique_target):
            counts = Counter()
            ans = left = 0
            cur_max = cur_min = 0
            for i,c in enumerate(s):
                counts[c] += 1
                while len(counts) > num_unique_target:
                    c0 = s[left]
                    counts[c0] -= 1
                    if counts[c0] == 0:
                        counts.pop(c0)
                    left += 1
                if all(v >= k for v in counts.values()):
                    ans = max(ans, i - left + 1)
            return ans

        upper_bound = sum(v >= k for v in Counter(s).values())
        ans = 0
        for num_unique_target in range(1, upper_bound + 1):
            ans = max(ans, longest_substr_with_n_unique(num_unique_target))
        return ans

        '''
        3/3 A complex implementation to find longest substr with x unique
        chars, but faster.

        Time: O(n) where n is len(s).
        Space: O(U).
        '''
        def longest_substr_with_n_unique(num_unique_target):
            freqs = Counter()
            num_unique = num_at_least_k = left = ans = 0
            for i in range(len(s)):
                char = s[i]
                if freqs[char] == 0:
                    num_unique += 1
                freqs[char] += 1
                if freqs[char] == k:
                    num_at_least_k += 1

                while num_unique > num_unique_target:
                    char = s[left]
                    if freqs[char] == k:
                        num_at_least_k -= 1
                    freqs[char] -= 1
                    if freqs[char] == 0:
                        num_unique -= 1
                    left += 1

                if num_unique == num_at_least_k:
                    ans = max(ans, i - left + 1)
            return ans

        upper_bound = sum(v >= k for v in Counter(s).values())
        ans = 0
        for num_unique_target in range(1, upper_bound + 1):
            ans = max(ans, longest_substr_with_n_unique(num_unique_target))
        return ans
        '''
        3/3
        '''