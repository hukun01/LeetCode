# 718. Maximum Length of Repeated Subarray
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        '''
        1/3 DP
        Similar to 1143. Longest Common Subsequence
        Let f[a][b] be the answer for A[:a] and B[:b]
        f[a][b] = f[a-1][b-1] + 1 if A[a-1] == B[b-1] else 0
        answer is max(f).

        Time: O(n1 * n2)
        Space: O(n1 * n2) can be reduced to O(min(n1, n2)), as f[a] depends on
        f[a-1].
        '''
        f = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        ans = 0
        for a in range(len(A) + 1):
            for b in range(len(B) + 1):
                if a - 1 >= 0 and b - 1 >= 0 and A[a - 1] == B[b - 1]:
                    f[a][b] = 1 + f[a - 1][b - 1]
                    ans = max(ans, f[a][b])

        return ans
        '''
        2/3 DP with constant space.

        Starting from each index i in n1, we fix the starting point as k, and
        compare A[k] and every B[j]. When A[k] == B[j], we increase the cur max
        len; Otherwise, we set the cur max len to 0, as we are finding a
        consecutive subarray.
        Do the similar process from n2 and compare with n1.
        Record the max len as the answer.

        Time: O(n1 * n2)
        Space: O(1)
        '''
        def find_max_match(arr1, arr2):
            ans = 0
            n1 = len(arr1)
            for i in range(n1):
                maxLenEnding = 0
                k = i
                for j in range(len(arr2)):
                    if k == n1:
                        break
                    if arr1[k] == arr2[j]:
                        maxLenEnding += 1
                        ans = max(ans, maxLenEnding)
                    else:
                        maxLenEnding = 0
                    k += 1
            return ans

        return max(find_max_match(A, B), find_max_match(B, A))
        '''
        3/3 Binary search + Rabin Karp rolling hash.

        Binary search the possible length of the subarray, and check the
        length using rolling hash.

        Time: O((n1 + n2) * log(min(n1, n2)))
        Space: O(n1 + n2)
        '''
        n1 = len(A)
        n2 = len(B)
        base = 103
        M = 10 ** 9 + 7
        def collect_hashes(arr, x):
            h = 0
            for i in range(x):
                h = (h * base + arr[i]) % M
            seen = {h}
            R = pow(base, x, M)
            for i in range(x, len(arr)):
                h = (h * base + M - R * arr[i-x] + arr[i]) % M
                seen.add(h)
            return seen

        def ok(x):
            return len(collect_hashes(A, x) & collect_hashes(B, x)) > 0

        l = 0
        h = min(n1, n2)
        while l < h:
            m = (l + h + 1) // 2
            if ok(m):
                l = m
            else:
                h = m - 1

        return l