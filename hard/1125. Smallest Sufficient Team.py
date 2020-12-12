# 1125. Smallest Sufficient Team
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        '''
        Memoized DFS with state compression using bit operations.
        
        To clear the k-th bit on an int i, use i & ~(1 << k).
        Note that in Py, 'not' op works on signed int, it may not be clear on
        intermediate result, but works fine on bitwise operations.
        '''
        n = len(req_skills)
        skillsToIdx = { x: i for i, x in enumerate(req_skills) }
        people = [[skillsToIdx[s] for s in skills if s in skillsToIdx] for skills in people]
        skillToPeople = defaultdict(list)
        for pIdx, skillIdxs in enumerate(people):
            for sIdx in skillIdxs:
                skillToPeople[sIdx].append(pIdx)

        @lru_cache(None)
        def dfs(skillsNeeded):
            if skillsNeeded == 0:
                return []
            ans = None
            neededSkillId = next(sIdx for sIdx in range(n) if skillsNeeded & (1 << sIdx))
            for nextPeople in skillToPeople[neededSkillId]:
                tmp = skillsNeeded
                for sIdx in people[nextPeople]:
                    tmp &= ~(1 << sIdx)
                curList = dfs(tmp)
                if ans is None or len(curList) + 1 < len(ans):
                    ans = curList + [nextPeople]
            return ans
        return dfs((1 << n) - 1)