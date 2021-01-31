# 756. Pyramid Transition Matrix
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        '''
        DFS.
        Focus on current line and the above line.
        '''
        rules = defaultdict(set)
        for a in allowed:
            rules[a[:2]].add(a[2])

        def dfs(cur_level, col, next_level):
            if 1 == len(cur_level):
                return True

            if col > len(cur_level):
                return dfs(next_level, 2, "")

            part = cur_level[col-2:col]
            for next_letter in rules[part]:
                if dfs(cur_level, col + 1, next_level + next_letter):
                    return True
            return False

        return dfs(bottom, 2, "")