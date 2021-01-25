# 753. Cracking the Safe
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        ans = []
        seen = set()
        def dfs(node):
            for i in range(k):
                nextNode = node + str(i)
                if nextNode not in seen:
                    seen.add(nextNode)
                    dfs(nextNode[1:])
                    ans.append(str(i))

        dfs("0" * (n - 1))
        return "".join(ans) + "0" * (n - 1)