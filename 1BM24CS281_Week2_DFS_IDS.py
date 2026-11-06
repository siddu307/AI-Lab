class EightPuzzle:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def find_blank(self, state):
        for r in range(3):
            for c in range(3):
                if state[r][c] == 0:
                    return r, c
        return None

    def get_neighbors(self, state):
        r, c = self.find_blank(state)
        neighbors = []
        for dr, dc in self.moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = [list(row) for row in state]
                new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
                neighbors.append(tuple(tuple(row) for row in new_state))
        return neighbors

    def print_path(self, path):
        for step, state in enumerate(path):
            print(f"Step {step}:")
            for row in state:
                print(" ".join(map(str, row)))
            print()

    def solve_dfs(self, max_depth=30):
        
        visited = set()
        path = []

        def dfs(current_state, depth):
            if current_state == self.goal_state:
                path.append(current_state)
                return True

            if depth >= max_depth:
                return False

            visited.add(current_state)
            path.append(current_state)

            for neighbor in self.get_neighbors(current_state):
                if neighbor not in visited:
                    if dfs(neighbor, depth + 1):
                        return True

            path.pop()
            visited.remove(current_state)
            return False

        if dfs(self.start_state, 0):
            return path
        return None

    def solve_ids(self, max_depth_limit=50):
        def depth_limited_search(current_state, limit, path, visited):
            if current_state == self.goal_state:
                return True, path

            if limit <= 0:
                return False, None

            visited.add(current_state)

            for neighbor in self.get_neighbors(current_state):
                if neighbor not in visited:
                    found, res_path = depth_limited_search(
                        neighbor, limit - 1, path + [neighbor], visited
                    )
                    if found:
                        return True, res_path

            visited.remove(current_state)
            return False, None

        for depth in range(max_depth_limit):
            visited = set()
            found, path = depth_limited_search(
                self.start_state, depth, [self.start_state], visited
            )
            if found:
                print(f"IDS found solution at depth limit: {depth}")
                return path
        return None
if __name__ == "__main__":
    initial_state = (
        (1, 2, 3),
        (8, 4, 5),
        (7, 0, 6)
    )

    goal_state = (
        (1, 2, 3),
        (8, 0, 4),
        (7, 6, 5)
    )

    puzzle = EightPuzzle(initial_state, goal_state)

    print("================ DFS Solution ================")
    dfs_path = puzzle.solve_dfs(max_depth=30)
    if dfs_path:
        print(f"DFS Path length: {len(dfs_path) - 1} moves")
        puzzle.print_path(dfs_path)
    else:
        print("No solution found within DFS max depth.")

    print("================ IDS Solution ================")
    ids_path = puzzle.solve_ids(max_depth_limit=50)
    if ids_path:
        print(f"IDS Path length: {len(ids_path) - 1} moves")
        puzzle.print_path(ids_path)
    else:
        print("No solution found within IDS depth limit.")
