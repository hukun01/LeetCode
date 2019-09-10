class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        '''
        Check the sequence of parenthesis using counter, increment 1 when seeing '(',
        decrement 1 when seeing ')'. When counter is negative, we have extra ')'.
        When seeing the first extra ')', recursively process each new string with one ')' removed
        from each possible position.
        When deleting ')', remember to skip the continuous duplicates.
        If there is no extra ')', meaning we have removed them all in the previous part, now we need
        to scan from right to left to ensure there is no extra '(', or we can exit the function after
        adding the current string to the result list.
        A good example to go through the code is "())())"
        '''
        ans = []

        # lastI denotes the s[:lastI] prefix that contains valid # of parens after the last removal,
        # lastJ denotes the last index that we removed the extra paren from the prefix.
        def dfs(s, lastI, lastJ, openParen, closedParen):
            counter = collections.Counter()
            i = lastI
            while i < len(s) and counter[closedParen] <= counter[openParen]:
                counter[s[i]] += 1
                i += 1
            if counter[closedParen] > counter[openParen]:
                # put i back to the right position as we incremented it before exiting the loop above,
                # now i points to the first extra ')'.
                i -= 1
                # now there is one extra ')' that we need to delete,
                # we can go back to delete one ')' from each position, skipping continuous duplicates.
                for j in range(lastJ, i+1):
                    if s[j] == closedParen and (j == lastJ or s[j-1] != closedParen):
                        # effectively removing s[j], and continue the processing with recursion,
                        # note that now the first i elements contain valid # of parenthesis.
                        dfs(s[:j] + s[j+1:], i, j, openParen, closedParen)
            else:
                # no extra ')', now we need to scan from right to left, or to exit the whole function.
                if openParen == '(':
                    # we've processed from left to right, now reverse
                    # the input and parenthesis, to process from right to left.
                    dfs(s[::-1], 0, 0, ')', '(')
                else:
                    ans.append(s[::-1])
        dfs(s, 0,0,'(', ')')
        return ans
        