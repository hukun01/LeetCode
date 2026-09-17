# 71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        The key is to be detail oriented, carefully evaluate each
        situation before committing.
        Note that when the current dir is at the root, going to the
        parent dir, aka, '..', is still valid.

        Since we skip '', we won't have the root dir in the final stack,
        so we should always add it to the head of the path.
        '''
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
