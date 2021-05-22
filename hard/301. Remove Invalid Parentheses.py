# 301. Remove Invalid Parentheses
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        '''
        1/2 BFS.
        The key is to stop further BFS once the longest valid parens are found.
        '''
        def valid(x):
            left = 0
            for c in x:
                if c == '(':
                    left += 1
                elif c == ')':
                    if left == 0:
                        return False
                    left -= 1

            return left == 0

        q = deque([s])
        used = set()
        found = False
        ans = []
        while q and not found:
            for _ in range(len(q)):
                node = q.popleft()
                if node in used:
                    continue
                used.add(node)
                if valid(node):
                    found = True
                    ans.append(node)

                for i in range(len(node)):
                    if node[i] not in '()':
                        continue
                    new = node[:i] + node[i+1:]
                    q.append(new)

        return ans
        '''
        2/2 Recursive DFS.
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

        # last_i denotes the s[:last_i] prefix that contains valid # of parens after the last removal,
        # last_j denotes the last index that we removed the extra paren from the prefix.
        def dfs(s, last_i, last_j, open_paren, closed_paren):
            counter = Counter()
            i = last_i
            while i < len(s) and counter[closed_paren] <= counter[open_paren]:
                counter[s[i]] += 1
                i += 1
            if counter[closed_paren] > counter[open_paren]:
                # put i back to the right position as we incremented it before exiting the loop above,
                # now i points to the first extra ')'.
                i -= 1
                # now there is one extra ')' that we need to delete,
                # we can go back to delete one ')' from each position, skipping continuous duplicates.
                for j in range(last_j, i+1):
                    if s[j] == closed_paren and (j == last_j or s[j-1] != closed_paren):
                        # effectively removing s[j], and continue the processing with recursion,
                        # note that now the first i elements contain valid # of parenthesis.
                        dfs(s[:j] + s[j+1:], i, j, open_paren, closed_paren)
            else:
                # no extra ')', now we need to scan from right to left, or to exit the whole function.
                if open_paren == '(':
                    # we've processed from left to right, now reverse
                    # the input and parenthesis, to process from right to left.
                    dfs(s[::-1], 0, 0, ')', '(')
                else:
                    ans.append(s[::-1])
        dfs(s, 0, 0, '(', ')')
        return ans