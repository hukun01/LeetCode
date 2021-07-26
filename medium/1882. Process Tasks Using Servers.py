# 1882. Process Tasks Using Servers
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        '''
        Heaps.

        Keep track of 2 heaps, one about free servers, another about working
        servers. The free servers heap prioritizes the servers with the
        smallest weights and server index. The working servers prioritizes the
        servers with the smallest task finish time and server index.

        Go through the tasks, for each task, take the first free server, add it
        to working servers. The key is to 'bump' the cur_time to the next
        working server's task finish time, when there's no free servers. This
        ensures that there will be at least one free server added from working
        server in the next step.

        Time: O(T log(S)) where T is len(tasks), S is len(servers).
        Space: O(T + S)
        '''
        free_servers = [
            (server_weight, i) for i, server_weight in enumerate(servers)]
        heapify(free_servers)

        # heap of (task_finish_time, server_idx)
        busy_servers = []
        ans = []
        cur_time = 0
        for task_idx, task_time in enumerate(tasks):
            if not free_servers:
                cur_time = busy_servers[0][0]
            while busy_servers and busy_servers[0][0] <= cur_time:
                _, server_idx = heappop(busy_servers)
                heappush(free_servers, (servers[server_idx], server_idx))

            _, server_idx = heappop(free_servers)
            heappush(busy_servers, (cur_time + task_time, server_idx))
            ans.append(server_idx)

            cur_time = max(task_idx + 1, cur_time)

        return ans