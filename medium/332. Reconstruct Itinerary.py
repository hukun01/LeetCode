class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        Note that if there is a dead-ended path, there can only be one such path,
        and the other path would be a circle.
        Based on this attribute, if we go into a dead end, the previous node must
        have another branch to go. Also, when we finish the recursion on dead-ended path,
        we can add the nodes to the route, because they will be the ending part.
        Remember to reverse the route before returning.
        '''
        targets = collections.defaultdict(list)
        for t in sorted(tickets)[::-1]:
            targets[t[0]].append(t[1])
        
        ans = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            ans.append(airport)
                
        visit("JFK")
        return ans[::-1]