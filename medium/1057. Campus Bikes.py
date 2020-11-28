class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        '''
        1/2 Heap

        A naive thought would be to do BFS from each worker to find the closest unused bike,
        but it would be too many steps to explore - 1000^2 for each worker, totally (1000^2) * W, worse case 1000^3.
        
        Instead, we can list out all the possible worker-bike assignments, and we will have
        a list of W lists, i-th list has all bikes sorted by distance to that worker i. And we sort the head
        of W lists, and pick from the shortest distance. If the bike is used, we move to the next element
        in that list. This now becomes merging W lists. The time would be W(BlogB) [building the list of W lists, in which
        each list has B sorted elements] + WlogB [merging W lists with B length, up to W times]. The time would be O(WBlogB).

        For each worker, create a reversely sorted list of (distance, wIdx, bIdx) tuples.
        
        Build a bike heap by poping each worker's bike list.
        
        Keep poping the bike heap until we assign each worker a bike. Note that we can add
        more bikes to the bike heap from the worker's bike list.
        
        The way we use bike heap is a bit similar to "merge n sorted lists".
        '''

        distances = [] # a list of lists, each list stores all (distance, bike) for a worker
        for wIdx in range(len(workers)):
            w = workers[wIdx]
            distances.append([])
            for bIdx in range(len(bikes)):
                d = sum(abs(c1 - c2) for c1, c2 in zip(w, bikes[bIdx]))
                distances[-1].append((d, wIdx, bIdx))
            distances[-1].sort(reverse = True)

        ans = [0] * len(workers)
        usedBikes = set()
        sortedBikes = [distances[i].pop() for i in range(len(workers))]
        heapify(sortedBikes)
        while sortedBikes:
            d, wIdx, bIdx = heappop(sortedBikes)
            if bIdx not in usedBikes:
                ans[wIdx] = bIdx
                usedBikes.add(bIdx)
            else:
                heappush(sortedBikes, distances[wIdx].pop())
        return ans
        '''
        2/2 Bucket sort
        We know that the coordinates fall into [0, 1000), so the distance is less than 2000.
        Based on this fact we can use bucket sort. For each distance, we list out the (worker, bike)
        tuples, and iterate through the tuple list from the lowest distance.


        distances = [[] for i in range(2000)]
        for wIdx, (x, y) in enumerate(workers):
            for bIdx, (x_b, y_b) in enumerate(bikes):
                distance = abs(x - x_b) + abs(y - y_b)
                distances[distance].append((wIdx, bIdx))
        used_bikes = set()
        assignments = [-1] * len(workers)
        for distance in distances:
            for worker, bike in distance:
                if assignments[worker] == -1 and bike not in used_bikes:
                    used_bikes.add(bike)
                    assignments[worker] = bike
        return assignments
        '''