from collections import deque


def bfs(start, goals, grid, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    distances = [[float('inf')] * m for _ in range(n)]

    if isinstance(start, list):
        for sx, sy in start:
            if grid[sx][sy] == '.':
                queue.append((sx, sy))
                distances[sx][sy] = 0
    else:
        if grid[start[0]][start[1]] == '.':
            queue.append(start)
            distances[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.':
                if distances[nx][ny] > distances[x][y] + 1:
                    distances[nx][ny] = distances[x][y] + 1
                    queue.append((nx, ny))

    min_distance = float('inf')
    for gx, gy in goals:
        if distances[gx][gy] < min_distance:
            min_distance = distances[gx][gy]

    return min_distance if min_distance != float('inf') else -1


def solution(n, m, k, xy, grid):
    # Find initial positions for S and F
    sx = sy = fx = fy = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                sx, sy = i, j
            elif grid[i][j] == 'F':
                fx, fy = i, j

    # Convert button coordinates and find adjacent free cells
    button_positions = [(x - 1, y - 1) for x, y in xy]
    reachable_buttons = []
    for x, y in button_positions:
        adj_cells = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.':
                adj_cells.append((nx, ny))
        reachable_buttons.append(adj_cells)

    # Calculate distances from S to first button
    initial_distances = bfs((sx, sy), reachable_buttons[0], grid, n, m)
    if initial_distances == -1:
        return -1

    total_min_time = initial_distances

    # Calculate distances between consecutive button presses
    for i in range(k - 1):
        distance = bfs(reachable_buttons[i], reachable_buttons[i + 1], grid, n, m)
        if distance == -1:
            return -1
        total_min_time += distance

    # Calculate distances from last button to F
    final_distance = bfs(reachable_buttons[-1], [(fx, fy)], grid, n, m)
    if final_distance == -1:
        return -1
    total_min_time += final_distance

    return total_min_time


def main():
    n, m, k = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    xy = [tuple(map(int, input().split())) for _ in range(k)]
    result = solution(n, m, k, xy, grid)
    print(result)


if __name__ == "__main__":
    main()
