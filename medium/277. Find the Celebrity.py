# 277. Find the Celebrity
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        '''
        The key is that there can be at most one celebrity, because
        celebrities don't know others, but the definition of celebrity
        also mentions that celebrity needs to be known by everyone.
        Hence, we don't have to scan the whole social network which is O(n^2) time,
        but just find the single candidate who doesn't know anyone,
        and confirm that everyone knows this candidate.
        '''
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        # candidate doesn't know anyone after self

        for i in range(n):
            if i != candidate:
                if knows(candidate, i) or not knows(i, candidate):
                    return -1

        return candidate