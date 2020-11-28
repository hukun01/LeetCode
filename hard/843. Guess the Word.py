# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        '''
        1/2 Exclude impossible similar words using the word with the most
        frequent characters

        For each position, count the total number of characters on that
        position, then use the word with the most frequent chars on all
        positions. We have no idea if this word would be the secret word.
        based on probability, (25/26)^8 ~ 80% chance that a random word will
        have 0 match with the secret, but since our word has the most frequent
        total chars, it's very likely that this word will have some match with
        many words, including the secret. If it doesn't match the secret, we
        can exclude many words that are similar to it, so to largely reduce
        the guess space for the next iteration.
        '''
        def similar(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        score = 0
        while score < 6:
            count = [Counter(w[i] for w in wordlist) for i in range(6)]
            guess = max(wordlist, key=lambda w: sum(count[i][c] for i, c in enumerate(w)))
            score = master.guess(guess)
            wordlist = [w for w in wordlist if similar(w, guess) == score]

        '''
        2/2 Exclude impossible similar words using the most 0 match word

        Probabilistically, (25/26)^8 ~ 80% in the words will have 0 match
        with the secret. With 80% chance, we can eliminate a wrong word and
        all its similar words that have 1+ matches with it.
        
        Hence we start with a word that has minimum 0 matches with every other
        words, meaning the one that has the most similar words. And with 80%
        chance we can eliminate this big chunk of similar words.
        '''
        def similar(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))
        score = 0
        while score != 6:
            words = Counter()
            for w1, w2 in itertools.combinations(wordlist, 2):
                if similar(w1, w2):
                    words[w1] += 1
                    words[w2] += 1
            w = wordlist[0]
            w = next(iter(key for key in words if words[key] > words[w]), w)
            score = master.guess(w)
            wordlist = [w1 for w1 in wordlist if score == similar(w, w1)]