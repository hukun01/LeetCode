class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        Topological sorting.
        Find the prerequisite pairs by iterating every 2 words, and do topological sorting
        on the pair list.
        '''
        pre_count = defaultdict(int)
        succ = defaultdict(list)
        for w1, w2 in zip(words, words[1:]):
            chars = next(((c1, c2) for c1, c2 in zip(w1, w2) if c1 != c2), None)
            if chars:
                (pre, post) = chars
                pre_count[post] += 1
                succ[pre].append(post)
            else:
                if len(w1) > len(w2):
                    return ""
        ans = []
        all_chars = set(c for c in itertools.chain(*words))
        free = all_chars - set(pre_count)
        while free:
            a = free.pop()
            ans.append(a)
            for b in succ[a]:
                pre_count[b] -= 1
                pre_count[b] or free.add(b)

        return "".join(ans) if len(ans) == len(all_chars) else ""
        '''
        Another implementation.
        To make code concise, use list comprehension as much as possible.

        No need to use defaultdict because we actually need to explicitly
        keep all chars in the dict.
        '''
        prevs = { c: set() for c in itertools.chain(*words) }
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    prevs[c2].add(c1)
                    break
            else:
                if len(w1) > len(w2):
                    return ""
        ans = []
        while True:
            removed = { c for c, prev in prevs.items() if len(prev) == 0 }
            if len(removed) == 0:
                break
            ans += removed
            prevs = { c: prevSet - removed for c, prevSet in prevs.items() if len(prevSet) > 0 }
        return ''.join(ans) if len(prevs) == 0 else ""