def solution(n, arr) -> tuple[int, list[int]]:
    dist = [float('inf')] * n
    pred = [-1] * n
    dist[0] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if arr[u][v] != 100000 and dist[u] + arr[u][v] < dist[v]:
                    dist[v] = dist[u] + arr[u][v]
                    pred[v] = u

    for u in range(n):
        for v in range(n):
            if arr[u][v] != 100000 and dist[u] + arr[u][v] < dist[v]:
                cycle = []
                for _ in range(n):
                    v = pred[v]

                cycle_start = v
                visited = set()
                while cycle_start not in visited:
                    visited.add(cycle_start)
                    cycle.append(cycle_start + 1)
                    cycle_start = pred[cycle_start]

                cycle = cycle[cycle.index(cycle_start + 1):]

                return len(cycle), cycle

    return 0, []


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    arr = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index + n]))
        arr.append(row)
        index += n

    count, verts = solution(n, arr)
    if not count:
        print('NO')
        return
    print('YES')
    print(count)
    print(' '.join(map(str, verts)))


if __name__ == '__main__':
    main()
