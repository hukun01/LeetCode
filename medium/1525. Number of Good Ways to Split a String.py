# 1525. Number of Good Ways to Split a String
class Solution:
    '''
    Sliding window.
    We start from index 0, the right chars frequency is the total chars
    frequency, called 'right_count'. We then iterate through s, as we move the
    index with char 'a', we increment left_count[a] and decrement
    right_count[a], whenever right_count[a] == 0, we pop 'a' out.
    Whenever len(left_count) == len(right_count), we have a good split.

    Time: O(n) where n is len(s)
    Space: O(1) since there are at most 26 chars.
    '''
    def numSplits(self, s: str) -> int:
        right_count = Counter(s)
        left_count = Counter()
        ans = 0
        for a in s:
            left_count[a] += 1
            right_count[a] -= 1
            if right_count[a] == 0:
                right_count.pop(a)

            if len(left_count) == len(right_count):
                ans += 1
        return ans