class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        The smallest subseq in lexicographical order, is the increasing
        subseq among all subseqs.
        When seeing a char, the decision we make is whether this char 'c' is
        the smallest char we can add to the subseq. We tell this by comparing
        'c' with the last char - if 'c' is smaller than the last char, we can
        pop out the last char and put 'c' there, only if we can get the last
        char later from 's'.

        Use a stack because we are only interested in the most recent chars. 

        If:
            1. current char is a new char we have not used,
            2. and it is smaller than the last char in stack,
            3. and the last char appears later in the string again,
        then:
            the last char can be removed and added later.
        E.g., stack = "bc", and remaining string is "abc" then 'a' can pop 'c' and then 'b'.

        Use a counter to tell whether a char appears later in the string again.
        Use a set to tell whether we already added the char to the answer.

        Note that the stack is monotonically increasing, so when we see a visited char,
        we should skip it, because it must have been put in the right place. Only new
        char can cause potential rearrangement.
        '''
        remainingLetters = Counter(s)
        visited = set()
        stack = []
        for c in s:
            remainingLetters[c] -= 1
            if c in visited: # c has been added in the earlier position
                continue
            while stack and c < stack[-1] and remainingLetters[stack[-1]] > 0:
                lastChar = stack.pop()
                visited.remove(lastChar)
            stack.append(c)
            visited.add(c)
        return ''.join(stack)