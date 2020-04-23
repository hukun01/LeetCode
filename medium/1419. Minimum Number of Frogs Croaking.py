# 1419. Minimum Number of Frogs Croaking
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        '''
        Similar to the meeting room problem.
        Note that a char cannot outnumber its previous char in the 'croak'.
        Every time we see a 'c', we know a new frog joined.
        When we see a 'k', a frog has done finish the song, so he can leave.
        Record the max number of frogs in the above progress.
        At the end, if there is any frog left without finishing the song, return -1.
        '''
        croak = 'croak'
        letterToIdx = { c: i for i, c in enumerate(croak) }
        need = [0] * len(croak)
        frogs = ans = 0
        for c in croakOfFrogs:
            i = letterToIdx[c]
            if i == 0:
                need[i] += 1
                frogs += 1
            else:
                if need[i-1] > 0:
                    need[i] += 1
                    need[i-1] -= 1
                else:
                    return -1
                if i == len(croak) - 1:
                    frogs -= 1
            ans = max(ans, frogs)
        return ans if frogs == 0 else -1