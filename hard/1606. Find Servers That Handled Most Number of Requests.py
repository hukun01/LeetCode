# 1606. Find Servers That Handled Most Number of Requests
from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        '''
        SortedList.
        The key is to retrieve the next free server efficiently.
        Use a SortedList A to record the server busy time and server id.
        At each new request arrival time, move all freed servers from
        A to another SortedList B, from which we can binary search to find
        the next free server.
        '''
        available_servers = SortedList(range(k))
        free_server_events = SortedList()
        num_reqs = Counter()
        for i, (time, duration) in enumerate(zip(arrival, load)):
            while free_server_events and free_server_events[0][0] <= time:
                _, free_server_id = free_server_events.pop(0)
                available_servers.add(free_server_id)
            if len(available_servers) == 0:
                continue
            expected_server_id = i % k
            j = available_servers.bisect_left(expected_server_id) % len(available_servers)
            selected_server_id = available_servers.pop(j)
            num_reqs[selected_server_id] += 1
            free_server_events.add((time + duration, selected_server_id))

        max_num_reqs = max(num_reqs.values())
        return [i for i, count in num_reqs.items() if count == max_num_reqs]