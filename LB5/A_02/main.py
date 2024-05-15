import heapq


def solution(costs, roads):
    n = len(costs)

    graph = [[] for _ in range(n)]
    for a, b in roads:
        graph[a - 1].append((b - 1, costs[a - 1]))
        graph[b - 1].append((a - 1, costs[b - 1]))

    dist = [float('inf')] * n
    dist[0] = 0
    jerrycan = costs[0]

    pq = [(0, 0)]
    while pq:
        d, u = heapq.heappop(pq)

        if dist[u] < d:
            continue

        for v, c in graph[u]:
            new_d = d + c
            if new_d < dist[v]:
                dist[v] = new_d
                heapq.heappush(pq, (new_d, v))

            new_d_with_refuel = d + min(c, jerrycan)
            if new_d_with_refuel < dist[v]:
                dist[v] = new_d_with_refuel
                heapq.heappush(pq, (new_d_with_refuel, v))

                jerrycan -= min(c, jerrycan)
                if u != 0:
                    jerrycan = costs[u]

    return dist[n - 1] if dist[n - 1] != float('inf') else -1


def main():
    input()
    costs = list(map(int, input().split()))
    m = int(input())
    roads = []
    for _ in range(m):
        roads.append(list(map(int, input().split())))
    result = solution(costs, roads)
    print(result)


if __name__ == '__main__':
    main()
