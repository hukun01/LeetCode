# 316. Remove Duplicate Letters
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        Mono stack.
        The smallest subseq in lexicographical order, is the increasing
        subseq among all subseqs.
        When seeing a char, the decision we make is whether this char 'c' is
        the smallest char we can add to the subseq. We tell this by comparing
        'c' with the last char - if 'c' is smaller than the last char, and the
        last char will appear later, we can safely remove it now.

        Use a stack because we are only interested in the most recent chars. 

        E.g., stack = "bc", and remaining string is "abc" then 'a' can pop 'c'
        and then 'b'.

        Use a counter to tell whether a char appears later in the string.
        Use a set to tell whether we already added the char to the answer.

        Note that the stack is monotonically increasing, so when we see a
        visited char, we should skip it, because it must have been added to the
        right place. Only new char can cause potential rearrangement.

        Time: O(n) where n is len(s)
        Space: O(n)
        '''
        remaining_letters = Counter(s)
        visited = set()
        stack = []
        for c in s:
            remaining_letters[c] -= 1
            if c in visited: # c has been added in the earlier position
                continue
            while stack and c < stack[-1] and remaining_letters[stack[-1]] > 0:
                last_char = stack.pop()
                visited.remove(last_char)
            stack.append(c)
            visited.add(c)
        return ''.join(stack)