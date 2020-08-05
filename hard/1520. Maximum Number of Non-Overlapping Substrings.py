# 1520. Maximum Number of Non-Overlapping Substrings
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        '''
        Greedy.
        Find all the starts and ends for the intervals.
        Add the earliest-ending intervals that don't exceed themselves.

        Similar to finding the max number of meetings.
        '''
        starts = { c : s.index(c) for c in set(s) }
        ends = { c : s.rindex(c) for c in set(s) }
        
        ans, prev = [], -1
        for i in sorted(ends.values()):
            start, end = starts[s[i]], ends[s[i]]
            # ensure no longer substr appears in [start, end]
            j = end
            while j >= start and start > prev and end == i:
                start = min(start, starts[s[j]])
                end = max(end, ends[s[j]])
                j -= 1
            if start > prev and end == i:
                ans.append(s[start:end + 1])
                prev = end

        return ans