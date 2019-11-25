class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        '''
        1/2 Bucket sort
        We know that the coordinates fall into [0, 1000), so the distance is less than 2000.
        Based on this fact we can use bucket sort. For each distance, we list out the (worker, bike)
        tuples, and iterate through the tuple list from the lowest distance.
        '''
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
        2/2 Heap
        For each worker, create a reversely sorted list of (distance, wIdx, bIdx) tuples.
        
        Build a bike heap by poping each worker's bike list.
        
        Keep poping the bike heap until we assign each worker a bike. Note that we can add
        more bikes to the bike heap from the worker's bike list.
        
        The way we use bike heap is a bit similar to "merge n sorted lists".
        distances = [] # a list of heaps, each heap stores all (distance, bike) for a worker
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
        heapq.heapify(sortedBikes)
        while len(usedBikes) < len(workers):
            d, wIdx, bIdx = heapq.heappop(sortedBikes)
            if bIdx not in usedBikes:
                ans[wIdx] = bIdx
                usedBikes.add(bIdx)
            else:
                heapq.heappush(sortedBikes, distances[wIdx].pop())
        return ans
        '''