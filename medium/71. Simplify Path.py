# 71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for p in path.split('/'):
            if p in { '', '.' }:
                continue
            elif p == "..":
                if ans:
                    ans.pop()
            else:
                ans.append(p)
        return '/' + '/'.join(ans)