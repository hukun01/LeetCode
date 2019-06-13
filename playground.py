import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ADOBEC -> answer
        # ADOBECODEB[A] -> CODEBA
        # CODEBAN[C] -> BANC
        counter = collections.Counter()
        answer = 'a'.join([c for c in s])
        curr = collections.deque()
        targets = set(list(t))
        targetsCache = set(list(t))
        for c in s:
            counter[c] += 1
            curr.append(c)
            if c in targets:
                targets.remove(c)
            if curr[-1] == curr[0]:
                while curr and (curr[0] not in targetsCache or counter[curr[0]] > 1):
                    counter[curr.popleft()] -= 1
            if not targets and len(curr) < len(answer):
                answer = ''.join(curr)
        return answer

if __name__ == "__main__":
    so = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    x = so.minWindow(S, T)
    print("answer:", x)