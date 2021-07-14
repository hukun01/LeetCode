# 727. Minimum Window Subsequence
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        '''
        1/2 Binary search in s1

        In s1, find each char to its indexes mapping, so we know where to find
        the char in s1 later.
        Now iterate through s1, for each s1[i] that matches s2[0], we proceed.
        For every s2[i] in s2, we want to find the next matching index in s1,
        later than i1, and keep doing that until we find all s2 chars or fail.

        Time: O(n1 + k * n2 * log(n1)) where k is the count of s1[i] == s2[0].
        Space: O(n1) for the indexes
        '''
        n1 = len(s1)
        n2 = len(s2)
        start = 0
        size = inf
        pos = defaultdict(list)
        for i, c in enumerate(s1):
            pos[c].append(i)

        for i in range(n1 - n2 + 1):
            if s1[i] != s2[0]:
                continue
            found = True
            j = i + 1
            for need in s2[1:]:
                idx = bisect_left(pos[need], j)
                if idx == len(pos[need]):
                    found = False
                    break
                j = pos[need][idx] + 1
            if found and j - i < size:
                start = i
                size = j - i

        if size != inf:
            return s1[start: start + size]
        return ''
        '''
        2/2 State machine

        The first part is similar to 792. Number of Matching Subsequences.
        Build a mapping for s1 to track the index of each letter to the right
        to the current s1[i]. This way we know where to go to from any s1[i]
        to any next letter as we find in s2, in O(1) time.

        Then we collect the starting points from s1 that has the first char
        matched. And explore each starting point, with O(1) each step, and
        do that in O(n2) time.

        Time: O(26 * n1 + k * n2) where k is the count of s1[i] == s2[0].
        Space: O(26 * n1)
        '''
        n1 = len(s1)
        nexts = [[-1] * 26 for _ in range(n1 + 1)]
        s1 = s1
        for i in range(n1 - 1, -1, -1):
            if i+1 < n1:
                for ch in range(26):
                    nexts[i][ch] = nexts[i+1][ch]
            nexts[i][ord(s1[i]) - ord('a')] = i+1

        starts = []
        for i in range(n1):
            if s1[i] == s2[0]:
                starts.append(i)

        ans_start = -1
        ans_len = inf
        for i in starts:
            j = i
            found = True
            for ch in s2:
                j = nexts[j][ord(ch) - ord('a')]
                if j == -1:
                    found = False
                    break

            if found:
                if ans_start == -1 or j-i < ans_len:
                    ans_len = min(ans_len, j - i)
                    ans_start = i

        if ans_start == -1:
            return ""
        return s1[ans_start: ans_start + ans_len]