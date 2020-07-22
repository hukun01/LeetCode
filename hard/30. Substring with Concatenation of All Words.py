# 30. Substring with Concatenation of All Words
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        Sliding window.
        A key is that all words share the length, so we can use the same
        step size when iterating over the input string. Also, our starting
        point is from [0, word_len), instead of all indicies.
        '''
        if not words:
            return []
        word_len = len(words[0])
        ans = []
        expected = Counter(words)
        for i in range(word_len):
            window = Counter()
            word_count = 0
            for j in range(i, len(s), word_len):
                # it's ok for 'j + word_len' to exceed len(s), it would just
                # work like len(s) in that case.
                w = s[j: j + word_len]
                if w not in expected:
                    window.clear()
                    word_count = 0
                    continue
                window[w] += 1
                word_count += 1
                while expected[w] < window[w]:
                    pos = j - word_len * (word_count - 1)
                    removed_word = s[pos: pos + word_len]
                    window[removed_word] -= 1
                    word_count -= 1

                if word_count == len(words):
                    ans.append(j - word_len * (word_count - 1))
        return ans