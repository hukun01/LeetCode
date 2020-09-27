# 1601. Maximum Number of Achievable Transfer Requests
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        '''
        DFS.
        Brute force. Try adding each request, or not.
        Note that greedily finding the longest cycle would not work,
        because there can be two shorter cycles that add up to be
        more requests, and these two shorter cycles share edges with
        the longest cycle, so we can only use one of them.
        '''
        ans = sum(f == t for f, t in requests)
        requests = [[f, t] for f, t in requests if f != t]
        def dfs(idx, num, counts):
            if idx == len(requests):
                if all(c == 0 for c in counts):
                    return num
                return 0
            f, t = requests[idx]
            counts[f] -= 1
            counts[t] += 1
            ans = dfs(idx + 1, num + 1, counts)
            counts[f] += 1
            counts[t] -= 1
            ans = max(ans, dfs(idx + 1, num, counts))
            return ans
        return dfs(0, 0, [0] * n) + ans