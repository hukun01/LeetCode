# 780. Reaching Points
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        '''
        There are many branches from (sx, sy) to (tx, ty), all of which
        would not reach the end, except one path. From backward, there is
        only one path from (tx, ty) to (sx, sy).

        (tx, ty) comes from either:
        1. (tx' + k*ty, ty)
        2. (tx, ty' + k*tx)

        So tx' = tx - k*ty = tx % ty, if tx > ty
        or ty' = ty - k*tx = ty % tx, if ty > tx

        To handle cases like (1, 10000) where tx << ty, we use modulo, 
        otherwise the subtraction would take linear time.

        We keep tranforming tx and ty until tx <= sx or ty <= sy, then
        we check whether the diffs can be composed by one element, namely,
        either (sy, ty) % sx == 0 if sx == tx already,
        or     (sx, tx) % sy == 0 if sy == ty already.
        '''
        while tx > sx and ty > sy:
            if tx < ty:
                ty = ty % tx
            else:
                tx = tx % ty
        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
               sy == ty and sx <= tx and (tx - sx) % sy == 0