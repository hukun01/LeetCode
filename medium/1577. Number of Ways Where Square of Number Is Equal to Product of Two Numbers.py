# 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        1/2 Two sum.
        Same as 2sum problem, except that it's doing product instead of sum.

        Time: O(max(m^2, n^2)) where m, n is size of nums1, nums2, respectively.
        Space: O(max(m^2, n^2)) for the seen dictionaries.
        '''
        def get_seen(arr):
            seen = Counter()
            for i, a in enumerate(arr):
                for b in arr[i+1:]:
                    seen[a * b] += 1
            return seen

        seen1 = get_seen(nums1)
        seen2 = get_seen(nums2)
        a1 = sum(seen2[a * a] for a in nums1)
        a2 = sum(seen1[a * a] for a in nums2)
        return a1 + a2
        '''
        2/2 Optmized 2sum.
        Count the frequencies of arrays and sort them, this is to reduce
        duplicate numbers into counts.
        This has the best actual performance as it reduces duplicate numbers
        and search space.

        The key is to count the triplets of identical numbers with
        comb(count, 2).

        Time: O(max(mlogm, nlogn) + mn)
        where m, n is the unique numbers count of nums1, nums2.
        Space: O(max(m, n)) for the cache.
        '''
        nums1 = sorted(Counter(nums1).items())
        nums2 = sorted(Counter(nums2).items())
        def count(arr1, arr2):
            res = 0
            for a1, count1 in arr1:
                target = a1 ** 2
                l = 0
                r = len(arr2) - 1
                # Process arr2 when arr2[l] and arr2[r] are different.
                while l < r:
                    actual = arr2[l][0] * arr2[r][0]
                    if actual < target:
                        l += 1
                    elif actual > target:
                        r -= 1
                    else:
                        res += count1 * arr2[l][1] * arr2[r][1]
                        l += 1
                a2, count2 = arr2[l]
                # Process arr2 when arr2[l] and arr2[r] are the same.
                if a2 == a1: # equivalent to a2 ** 2 == target
                    res += count1 * math.comb(count2, 2)
            return res
        return count(nums1, nums2) + count(nums2, nums1)
        '''
        3/3 Combine the good parts above 2 methods.
        Do not sort arrays, and do frequency counts.
        This handles duplicates without having to sort the arrays,
        has the second best runtime performance.

        Time: O(max(m^2, n^2) + mn)
        where m, n is the unique numbers count of nums1, nums2.
        Space: O(max(m^2, n^2)) for the cache.
        '''
        nums1 = list(Counter(nums1).items())
        nums2 = list(Counter(nums2).items())

        def get_seen(arr):
            seen = Counter()
            for i, (a, count1) in enumerate(arr):
                seen[a * a] += math.comb(count1, 2)
                for b, count2 in arr[i+1:]:
                    seen[a * b] += count1 * count2
            return seen

        seen1 = get_seen(nums1)
        seen2 = get_seen(nums2)
        a1 = sum(count1 * seen2[a*a] for a, count1 in nums1)
        a2 = sum(count1 * seen1[a*a] for a, count1 in nums2)
        return a1 + a2