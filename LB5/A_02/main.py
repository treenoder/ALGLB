import heapq


def solution(n, costs, roads):
    n = len(costs)

    graph = [[] for _ in range(n)]
    for a, b in roads:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    pq = [(costs[0], 0, costs[0])]
    dist = [[float('inf')] * (max(costs) + 1) for _ in range(n)]
    dist[0][costs[0]] = costs[0]

    while pq:
        current_cost, u, jerry_can_fuel = heapq.heappop(pq)

        if u == n - 1:
            return current_cost

        for v in graph[u]:
            new_cost = current_cost + costs[u]
            if new_cost < dist[v][jerry_can_fuel]:
                dist[v][jerry_can_fuel] = new_cost
                heapq.heappush(pq, (new_cost, v, jerry_can_fuel))

            if jerry_can_fuel > 0:
                new_cost = current_cost
                new_jerry_can_fuel = max(0, jerry_can_fuel - costs[v])
                if new_cost < dist[v][new_jerry_can_fuel]:
                    dist[v][new_jerry_can_fuel] = new_cost
                    heapq.heappush(pq, (new_cost, v, new_jerry_can_fuel))

    return -1


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0

    n = int(data[idx])
    idx += 1
    costs = list(map(int, data[idx:idx + n]))
    idx += n

    m = int(data[idx])
    idx += 1
    roads = []
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx + 1])
        roads.append((a, b))
        idx += 2

    result = solution(n, costs, roads)
    print(result)


if __name__ == '__main__':
    main()
