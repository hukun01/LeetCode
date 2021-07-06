# 1062. Longest Repeating Substring
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        '''
        Binary search the substring window size.

        Notice that this problem has a monotic property - the larger the
        substring window is, the less likely we would find repeated substrings.

        Hence, we can binary search the window size M, and verify M in O(n)
        time.
        To verify M, we can collect all the substrings with size=M, and see
        if there's repetition. This takes O(n^2) space, and takes O(M(n-M))
        time. When M is close to n/2, this takes O(n^2) time.

        One thing to notice is that when doing binary search, we are actually
        searching for the minimum 'incompatible' M, and return M-1 as result.
        This is because when M=0, we can't collect substrings.

        Time: O(n log(n)) where n is len(s), and worst case O(n^2)
        Space: O(n^2)

        To improve the time and space, we can use rolling hash technique.
        However, as hash collision can happen in this process, we will need to
        double check the repeated strings to confirm, so complexity is added.
        '''
        n = len(s)
        def ok(window_size):
            seen = set()
            for i in range(0, n - window_size + 1):
                substr = s[i: i + window_size]
                if substr in seen:
                    return True
                seen.add(substr)
            return False

        l = 1
        h = n
        while l <= h:
            m = (l + h) // 2
            if ok(m):
                l = m + 1
            else:
                h = m - 1
        return l - 1