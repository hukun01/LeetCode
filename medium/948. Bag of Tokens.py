# 948. Bag of Tokens
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        '''
        Greedy.
        One token == 1 score, and 1 score can potentially become multiple
        tokens, in terms of token power.
        We keep taking score by spending smallest power on the smallest tokens,
        and keep taking the largest power from the largest tokens by spending 1
        score each time.
        '''
        ans = score = 0
        tokens = deque(sorted(tokens))
        power = P
        while tokens:
            if power >= tokens[0]:
                score += 1
                power -= tokens.popleft()
            elif score >= 1:
                score -= 1
                power += tokens.pop()
            else:
                break
            ans = max(ans, score)
        return ans