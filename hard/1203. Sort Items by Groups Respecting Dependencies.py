# 1203. Sort Items by Groups Respecting Dependencies
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        '''
        Topological sort.
        Two level topo sort.
        STEP 1: Create a new group for each item that belongs to no group. 
        STEP 2: Build directed graphs for items and groups.
        STEP 3: Find topological orders of items and groups.
        STEP 4: Find order of items within each group.
        STEP 5. Combine ordered groups.
        '''
        def get_top_order(graph, indegree):
            top_order = []
            free = [node for node in range(len(graph)) if indegree[node] == 0]
            while free:
                v = free.pop()
                top_order.append(v)
                for u in graph[v]:
                    indegree[u] -= 1
                    if indegree[u] == 0:
                        free.append(u)
            return top_order if len(top_order) == len(graph) else []

        # STEP 1: Create a new group for each item that belongs to no group. 
        for u in range(len(group)):
            if group[u] == -1:
                group[u] = m
                m += 1

        # STEP 2: Build directed graphs for items and groups.
        successors_item = [[] for _ in range(n)]
        indegree_items = [0] * n
        successors_group = [[] for _ in range(m)]
        indegree_groups = [0] * m        
        for cur, befores in enumerate(beforeItems):
            for prev in befores:
                successors_item[prev].append(cur)
                indegree_items[cur] += 1
                if (cur_group := group[cur]) != (prev_group := group[prev]):
                    successors_group[prev_group].append(cur_group)
                    indegree_groups[cur_group] += 1

        # STEP 3: Find topological orders of items and groups.
        sorted_items = get_top_order(successors_item, indegree_items)
        sorted_groups = get_top_order(successors_group, indegree_groups)
        if not sorted_items or not sorted_groups:
            return []

        # STEP 4: Find order of items within each group.
        items_to_group = defaultdict(list)
        for v in sorted_items:
            items_to_group[group[v]].append(v)

        # STEP 5. Combine ordered groups.
        return list(itertools.chain(*(items_to_group[g] for g in sorted_groups)))