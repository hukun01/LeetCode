class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ''' 
        Need to ensure that # of ) never surpasses # of (.
        We can add ( when the # of ( is below threshold;
        We can add ) only when # of ) is below # of (.
        '''
        ans = []
        def helper(curr, lefts, rights):
            if lefts == rights == n:
                ans.append(curr)
                return
            if lefts < n:
                helper(curr+'(', lefts+1, rights)
            if rights < lefts:
                helper(curr+')', lefts, rights+1)
        helper("", 0, 0)
        return ans