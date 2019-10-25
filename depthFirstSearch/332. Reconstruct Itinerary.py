class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for t in sorted(tickets)[::-1]:
            targets[t[0]].append(t[1])
        
        ans = []
        def dfs(airport):
            while targets[airport]:
                dfs(targets[airport].pop())
            ans.append(airport)
                
        dfs("JFK")
        return ans[::-1]