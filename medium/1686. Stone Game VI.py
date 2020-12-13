# 1686. Stone Game VI
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        '''
        Greedy + Sort.
        In Alice's turn she either gains the most for herself, or forces the
        most lost for Bob. Same applies to Bob.
        Hence, pick the most impactful stone for both, aka, the stone with the
        most total value, this way we gain the most or/and cause most lost at
        the same time.

        Time: O(n log(n)) for sort
        Space: O(n) for sort
        '''
        A = aliceValues
        B = bobValues
        n = len(A)
        a_b = sorted([(A[i] + B[i], i) for i in range(n)], reverse=True)
        alice = bob = 0
        alice_play = True
        for b_add_a, idx in a_b:
            if alice_play:
                alice += b_add_a - B[idx]
            else:
                bob += b_add_a - A[idx]
            alice_play = not alice_play

        if alice == bob:
            return 0
        elif alice > bob:
            return 1
        return -1