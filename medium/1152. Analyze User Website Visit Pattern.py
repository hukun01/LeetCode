# 1152. Analyze User Website Visit Pattern
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        '''
        Sort all visits by time, for each user, collect the visited websites.
        For each user, select the *distinct* website 3-sequence with
        combinations(), and count the frequency, finally return the one with
        max frequency and min website sequence.

        Time: O(max(n log(n), n!)) where n is len(username), and depend on
              how many distinct users and websites, the combination operation
              may need more time than the initial sort
        Space: O(n!)
        '''
        seq = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            seq[u].append(w)

        ans = Counter()
        for u, ws in seq.items():
            for triplet in set(combinations(ws, 3)):
                ans[triplet] += 1
        return list(min(ans.items(), key=lambda x: (-x[1], x[0]))[0])