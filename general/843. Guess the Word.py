# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        '''
        Probabilistically, (25/26)^8 ~ 80% in the words will have 0 match with the secret.
        With 80% chance, we can eliminate a wrong word and all its similar words that have 1+ matches with it.
        
        Hence we start with a word that has minimum 0 matches with every other words, meaning the one that has
        the most similar words. And with 80% chance we can eliminate this big chunk of similar words.
        '''
        def similarity(w1, w2):
            return sum(1 if c1 == c2 else 0 for c1, c2 in zip(w1, w2))
        
        while len(wordlist) > 1:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if similarity(w1, w2) == 0)
            guess = min(wordlist, key=lambda w: count[w])
            score = master.guess(guess)
            wordlist = [w for w in wordlist if similarity(w, guess) == score]