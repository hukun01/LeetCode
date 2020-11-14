# 458. Poor Pigs
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        '''
        Math.
        With 1 pig and T tests, we can test (T + 1) buckets, by making the
        pig drink the buckets one by one for T times, if it survives, then
        the last bucket that wasn't used is the poinsonous one.
        Basically a pig has (T + 1) states.
        With 2 pigs and 2 states (1 test), we can test 2 ^ 2 buckets, with
        below setup.
            pig1: bucket1, bucket2
            pig2: bucket2, bucket3
            After the first test, if both pigs died, it's due to bucket2;
            if only pig1 died, it's bucket1; if only pig2 died, it's bucket3;
            if both pigs survived, it's bucket4.
        In summary, with x pigs and y states, we can test y^x buckets, and
        y = T + 1, and y^x >= buckets, and we want to know x.
        With (T + 1) ^ x >= buckets, we have x >= log(buckets, (T + 1)), so
        x is the ceiling of that log.
        '''
        states = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets, states))