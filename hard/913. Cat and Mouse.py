# 913. Cat and Mouse
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        '''
        1/2 BFS + Topological sort.
        The MiniMax strategy may not work because there can be draw.
        Instead of top-down recursion, we do bottom-up BFS, starting from nodes
        that are sure-win, such as (mouse_pos = hole, cat_pos = any, any_turn)
        is mouse_win, (mouse_pos = x, cat_pos = x, any_turn) is cat_win.

        We expand from those finite positions in BFS, and record the neighbor
        nodes' statuses, based on 2 rules:
        1. If previous state is mouse_move, and current state is mouse_win,
           then the mouse would definitely goes from previouse state to current
           state, and win the game. Similar for cat. Thus, if this condition
           meets, we record the corresponding player as the winner. And if we
           revisit this state, we can skip it.
        2. If previous state's turn doesn't match the current winner, we know
           the previous state's turn player would not go to the current state.
           We track the outdegree for each state, in this case, we minus one
           from prev_state. When the outdegree[prev_state] == 0, we know that
           there's no choice for the prev_state but to let the current winner
           win.

        During the above process, whenever we find the start_state in winner
        record, we can end the game.
        '''
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
        MOUSE_MOVE, CAT_MOVE = 0, 1
        START_STATE = (1, 2, MOUSE_MOVE)
        HOLE = 0
        N = len(graph)
        outdegree = {}
        for mouse_pos in range(N):
            for cat_pos in range(N):
                outdegree[(mouse_pos, cat_pos, MOUSE_MOVE)] = len(graph[mouse_pos])
                outdegree[(mouse_pos, cat_pos, CAT_MOVE)] = len(graph[cat_pos]) - (HOLE in graph[cat_pos])

        winner = {}
        queue = deque() # store (mouse_pos, cat_pos, turn, who_win)
        for pos in range(N):
            for turn in (MOUSE_MOVE, CAT_MOVE):
                winner[(HOLE, pos, turn)] = MOUSE_WIN
                queue.append((HOLE, pos, turn, MOUSE_WIN))
                if pos != HOLE:
                    winner[(pos, pos, turn)] = CAT_WIN
                    queue.append((pos, pos, turn, CAT_WIN))

        def prev_states(mouse_pos, cat_pos, turn):
            if turn == CAT_MOVE:
                return [(pos, cat_pos, MOUSE_MOVE) for pos in graph[mouse_pos]]

            return [(mouse_pos, pos, CAT_MOVE) for pos in graph[cat_pos] if pos != HOLE]

        while queue:
            mouse_pos, cat_pos, turn, who_win = queue.popleft()
            for prev_mouse, prev_cat, prev_turn in prev_states(mouse_pos, cat_pos, turn):
                prev_state = (prev_mouse, prev_cat, prev_turn)
                if prev_state in winner:
                    continue

                if (prev_turn == MOUSE_MOVE and who_win == MOUSE_WIN) or \
                        (prev_turn == CAT_MOVE and who_win == CAT_WIN):
                    winner[prev_state] = who_win
                    queue.append((prev_mouse, prev_cat, prev_turn, who_win))
                else:
                    outdegree[prev_state] -= 1
                    if outdegree[prev_state] == 0:
                        winner[prev_state] = who_win
                        queue.append((prev_mouse, prev_cat, prev_turn, who_win))

            if START_STATE in winner:
                return winner[START_STATE]

        return DRAW
        '''
        2/2 Memoized DFS, MiniMax.
        Let m be the mouse position, c be the cat position.
        Three key rules:
        1. If it's mouse turn, and any next step leads to mouse win, then go
           down there. Otherwise, if there's a draw, go to draw. Otherwise,
           it's cat win.
        2. If it's cat turn, similar logic applies for cat, but note that cat
           can't go to hole.
        3. For the base case, the most critical condition is to return DRAW
           when there are 2n turn, where n is the number of nodes in graph.
           This is because, if mouse ignores cat, and go to hole directly, it
           will arrive within n step, but if mouse goes for n steps and still
           can't get to the hole, it must have stucked due to cat. And cat
           can't catch mouse either. They are both on some cycles. Hence it's
           a draw.

        Overall, DFS approach is a lot simpler, but it's unclear whether the
        above rule #3 is correct.

        Time: O(n^3) where n is len(graph)
        Space: O(n^3)
        '''
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
        HOLE = 0
        @lru_cache(None)
        def search(turn, m, c):
            if turn == 2 * len(graph): return DRAW
            if m == c: return CAT_WIN
            if m == HOLE: return MOUSE_WIN
            if turn % 2 == 0: # mouse turn
                if any(search(turn + 1, m_next, c) == MOUSE_WIN for m_next in graph[m]):
                    return MOUSE_WIN
                if any(search(turn + 1, m_next, c) == DRAW for m_next in graph[m]):
                    return DRAW
                return CAT_WIN
            else:
                if any(search(turn + 1, m, c_next) == CAT_WIN for c_next in graph[c] if c_next != HOLE):
                    return CAT_WIN
                if any(search(turn + 1, m, c_next) == DRAW for c_next in graph[c] if c_next != HOLE):
                    return DRAW
                return MOUSE_WIN

        return search(0, 1, 2)