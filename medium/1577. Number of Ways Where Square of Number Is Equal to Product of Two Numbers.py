# 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        1/2 Two sum.
        Same as 2sum problem, except that it's doing product instead of sum.
        Have a cache to the used target values to make it faster.
        Time: O(mn) where m, n is the size of nums1, nums2, respectively.
        Space: O(max(m, n)) for the cache.
        '''
        def find(target, arr):
            seen = Counter()
            count = 0
            for a in arr:
                if target % a == 0:
                    count += seen[target // a]
                seen[a] += 1
            return count
            
        @lru_cache(None)
        def twoProduct1(target):
            return find(target, nums1)

        @lru_cache(None)
        def twoProduct2(target):
            return find(target, nums2)

        return sum(twoProduct2(a*a) for a in nums1) + sum(twoProduct1(a*a) for a in nums2)
        '''
        2/2 Optmized 2sum.
        Count the frequencies of arrays and sort them, this is to reduce
        duplicate numbers into counts.
        This has the best actual performance as it reduces duplicate numbers
        and search space.
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
        This handles duplicates well without having to sort the arrays,
        has the second best runtime performance.
        Time: O(mn) where m, n is the unique numbers count of nums1, nums2.
        Space: O(max(m, n)) for the cache.
        '''
        nums1 = list(Counter(nums1).items())
        nums2 = list(Counter(nums2).items())
        def twoProduct(target, count1, arr):
            seen = Counter()
            ans = 0
            for a, count2 in arr:
                if target % a == 0:
                    if (b := target // a) != a:
                        ans += count1 * count2 * seen[b]
                    else:
                        ans += count1 * math.comb(count2, 2)
                seen[a] += count2
            return ans
        a1 = sum(twoProduct(a*a, c, nums2) for a, c in nums1)
        a2 = sum(twoProduct(a*a, c, nums1) for a, c in nums2)
        return a1 + a2