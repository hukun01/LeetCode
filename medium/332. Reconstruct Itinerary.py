class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        1/2 Brute force DFS.
        '''
        graph = defaultdict(list)
        for cur, nex in sorted(tickets):
            graph[cur].append(nex)

        self.ans = []
        visited = set()

        def dfs(cur, path):
            if len(path) == len(tickets) + 1:
                self.ans = path
                return True

            # Need to use index because there can be duplicate cities.
            for i, nex in enumerate(graph[cur]):
                if (cur, i) in visited:
                    continue
                visited.add((cur, i))
                if dfs(nex, path + [nex]):
                    return True
                visited.remove((cur, i))

            return False

        dfs('JFK', ['JFK'])

        return self.ans
        '''
        2/2 DFS based on finding Euler Path.

        Note that if there is a dead-ended path, there can only be one such
        path, and the other path would be a circle.
        Based on this attribute, if we go into a dead end, the previous node
        must have another branch to go. Also, when we finish the recursion on
        dead-ended path, we can add the nodes to the route, because they will
        be the ending part.
        Remember to reverse the route before returning.

        '''
        graph = defaultdict(list)
        for cur, nex in sorted(tickets)[::-1]:
            graph[cur].append(nex)

        ans = []
        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            ans.append(airport)

        visit("JFK")
        return ans[::-1]