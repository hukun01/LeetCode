# 780. Reaching Points
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        '''
        There are many branches from (sx, sy) to (tx, ty), all of which
        would not reach the end, except one path. From backward, there is
        only one path from (tx, ty) to (sx, sy).
        Assuming tx < ty, we have (tx, ty) -> (tx, ty - tx) ->..-> (sx, sy).
        To handle cases like (1, 10000) where tx << ty, we use modulo, 
        otherwise the subtraction would take linear time.
        '''
        while tx > sx and ty > sy:
            if tx < ty:
                ty = ty % tx
            else:
                tx = tx % ty
        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
               sy == ty and sx <= tx and (tx - sx) % sy == 0