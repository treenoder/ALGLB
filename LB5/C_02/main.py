def solution(n, arr):
    def find_negative_cycle():
        dist = [float('inf')] * n
        pred = [-1] * n

        for src in range(n):
            dist[src] = 0
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
                        x = v
                        for _ in range(n):
                            x = pred[x]

                        cycle_start = x
                        while True:
                            cycle.append(cycle_start + 1)
                            cycle_start = pred[cycle_start]
                            if cycle_start + 1 in cycle:
                                cycle.append(cycle_start + 1)
                                break

                        cycle.reverse()
                        cycle = cycle[cycle.index(cycle_start + 1):-1]

                        return len(cycle), cycle

        return 0, []

    return find_negative_cycle()


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
