def solution(n, m, edges):
    inf = 30000
    dist = [inf] * n
    dist[0] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u - 1] != inf and dist[u - 1] + w < dist[v - 1]:
                dist[v - 1] = dist[u - 1] + w

    dist = [d if d != inf else 30000 for d in dist]

    return dist


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])

    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        edges.append((u, v, w))
        index += 3
    res = solution(n, m, edges)
    print(*res)


if __name__ == '__main__':
    main()
