# 679. 24 Game
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        '''
        DFS.

        Base case: if len(cards) == 1, return whether it's close to 24. Note
        that there's a built-in method for this check `math.isclose()`.

        Then: generate all the permutations of cards, and take the first two
        to produce all possible results, and combine the result with the rest
        of the cards and do recursion. If any of the calls return true we can
        return.

        Note: when producing all possible results from a and b, it's possible
        that b is 0, so we need to check by `b and a/b`. In case b=0, this will
        evaluate to 0 just like a * b, but since we use set() to hold the
        results, we only get one 0.

        Time: O(A B) where A is number of all operand permutations (4*3*2),
            and B is the number of all operator permutations (4*4*4*2*2), the
            last two 2s are for parenthesis.
        Space: O(1), but we can also make this O(A) by caching all input. This
            works better when there're many duplicate input.
        '''
        if len(cards) == 1:
            return math.isclose(cards[0], 24)

        for a, b, *rest in permutations(cards):
            for x in {a+b, a-b, a*b, b and a/b}:
                if self.judgePoint24([x] + rest):
                    return True

        return False