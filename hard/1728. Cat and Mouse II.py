# 1728. Cat and Mouse II
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        '''
        1/2 BFS + Topological sort.
        Same as 913. Cat and Mouse.
        The difference here is to massage the input into graph.
        Note that mouse and cat uses different graph, due to different jumps.
        '''
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
        MOUSE_TURN, CAT_TURN = 'M', 'C'
        R, C = len(grid), len(grid[0])
        init_pos = {
            grid[r][c]: (r, c)
            for r in range(R) for c in range(C)
            if grid[r][c] in 'MCF'
        }

        init_mouse_pos = init_pos['M']
        init_cat_pos = init_pos['C']
        food_pos = init_pos['F']

        START_STATE = (init_mouse_pos, init_cat_pos, MOUSE_TURN)

        winner = {}
        G_mouse, G_cat = defaultdict(set), defaultdict(set)
        queue = deque() # (mouse_pos, cat_pos, turn, who_win)
        outdegree = {}
        def all_positions():
            for r in range(R):
                for c in range(C):
                    if grid[r][c] == '#': continue
                    yield (r, c)

        def last_positions(pos, jump):
            r, c = pos
            yield r, c
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                for k in range(1, jump + 1):
                    nr, nc = r + k * dr, c + k * dc
                    if not (0 <= nr < R and 0 <= nc < C): break
                    if grid[nr][nc] == '#': break
                    yield nr, nc
        
        for pos in all_positions():
            for turn in (MOUSE_TURN, CAT_TURN):
                winner[(pos, pos, turn)] = CAT_WIN
                winner[(pos, food_pos, turn)] = CAT_WIN
                winner[(food_pos, pos, turn)] = MOUSE_WIN
                queue.append((food_pos, pos, turn, MOUSE_WIN))
                queue.append((pos, food_pos, turn, CAT_WIN))
                queue.append((pos, pos, turn, CAT_WIN))

            G_mouse[pos] = set(last_positions(pos, mouseJump))
            G_cat[pos] = set(last_positions(pos, catJump))
        
        outdegree = Counter()
        for mouse_pos in all_positions():
            for cat_pos in all_positions():
                outdegree[(mouse_pos, cat_pos, MOUSE_TURN)] = len(G_mouse[mouse_pos])
                outdegree[(mouse_pos, cat_pos, CAT_TURN)] = len(G_cat[cat_pos])

        def prev_states(mouse_pos, cat_pos, turn):
            if turn == CAT_TURN:
                return [(pos, cat_pos, MOUSE_TURN) for pos in G_mouse[mouse_pos]]

            return [(mouse_pos, pos, CAT_TURN) for pos in G_cat[cat_pos]]

        while queue:
            mouse_pos, cat_pos, turn, who_win = queue.popleft()
            for prev_mouse, prev_cat, prev_turn in prev_states(mouse_pos, cat_pos, turn):
                prev_state = (prev_mouse, prev_cat, prev_turn)
                if prev_state in winner:
                    continue

                if (prev_turn == MOUSE_TURN and who_win == MOUSE_WIN) or \
                        (prev_turn == CAT_TURN and who_win == CAT_WIN):
                    winner[prev_state] = who_win
                    queue.append((prev_mouse, prev_cat, prev_turn, who_win))
                else:
                    outdegree[prev_state] -= 1
                    if outdegree[prev_state] == 0:
                        winner[prev_state] = who_win
                        queue.append((prev_mouse, prev_cat, prev_turn, who_win))

            if START_STATE in winner:
                return winner[START_STATE] == MOUSE_WIN

        return False
        '''
        2/2 Memoized DFS, MiniMax.
        Same as 913. Cat and Mouse.
        '''
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
        MOUSE_TURN, CAT_TURN = 'M', 'C'
        R, C = len(grid), len(grid[0])
        init_pos = {
            grid[r][c]: (r, c)
            for r in range(R) for c in range(C)
            if grid[r][c] in 'MCF'
        }

        food_pos = init_pos['F']

        def last_positions(pos, jump):
            r, c = pos
            yield r, c
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                for k in range(1, jump + 1):
                    nr, nc = r + k * dr, c + k * dc
                    if not (0 <= nr < R and 0 <= nc < C): break
                    if grid[nr][nc] == '#': break
                    yield nr, nc

        G_mouse, G_cat = defaultdict(set), defaultdict(set)
        def get_all_positions():
            for r in range(R):
                for c in range(C):
                    if grid[r][c] == '#': continue
                    yield (r, c)
        
        for pos in get_all_positions():
            G_mouse[pos] = set(last_positions(pos, mouseJump))
            G_cat[pos] = set(last_positions(pos, catJump))

        @lru_cache(None)
        def search(turn, m, c):
            if turn == 2 * R * C: return DRAW
            if c in {m, food_pos}: return CAT_WIN
            if m == food_pos: return MOUSE_WIN
            if turn % 2 == 0: # mouse turn
                if any(search(turn + 1, m_next, c) == MOUSE_WIN for m_next in G_mouse[m]):
                    return MOUSE_WIN
                if any(search(turn + 1, m_next, c) == DRAW for m_next in G_mouse[m]):
                    return DRAW
                return CAT_WIN
            else:
                if any(search(turn + 1, m, c_next) == CAT_WIN for c_next in G_cat[c]):
                    return CAT_WIN
                if any(search(turn + 1, m, c_next) == DRAW for c_next in G_cat[c]):
                    return DRAW
                return MOUSE_WIN

        return search(0, init_pos['M'], init_pos['C']) == MOUSE_WIN