import heapq


def solution(n, costs, roads):
    graph = [[] for _ in range(n)]
    for a, b in roads:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    pq = [(costs[0], 0, 1, 0)]
    dist = {}

    while pq:
        total_cost, u, fuel_in_tank, fuel_in_jerry_can = heapq.heappop(pq)

        if u == n - 1:
            return total_cost

        if (u, fuel_in_tank, fuel_in_jerry_can) in dist and dist[(u, fuel_in_tank, fuel_in_jerry_can)] <= total_cost:
            continue

        dist[(u, fuel_in_tank, fuel_in_jerry_can)] = total_cost

        for v in graph[u]:
            if fuel_in_tank > 0:
                new_total_cost = total_cost
                new_fuel_in_tank = fuel_in_tank - 1
                new_fuel_in_jerry_can = fuel_in_jerry_can
                if (v, new_fuel_in_tank, new_fuel_in_jerry_can) not in dist or new_total_cost < dist[
                    (v, new_fuel_in_tank, new_fuel_in_jerry_can)]:
                    heapq.heappush(pq, (new_total_cost, v, new_fuel_in_tank, new_fuel_in_jerry_can))

            if fuel_in_jerry_can > 0:
                new_total_cost = total_cost
                new_fuel_in_tank = 0
                new_fuel_in_jerry_can = fuel_in_jerry_can - 1
                if (v, new_fuel_in_tank, new_fuel_in_jerry_can) not in dist or new_total_cost < dist[
                    (v, new_fuel_in_tank, new_fuel_in_jerry_can)]:
                    heapq.heappush(pq, (new_total_cost, v, new_fuel_in_tank, new_fuel_in_jerry_can))

            new_total_cost = total_cost + costs[u]
            new_fuel_in_tank = 1
            new_fuel_in_jerry_can = fuel_in_jerry_can
            if (u, new_fuel_in_tank, new_fuel_in_jerry_can) not in dist or new_total_cost < dist[
                (u, new_fuel_in_tank, new_fuel_in_jerry_can)]:
                heapq.heappush(pq, (new_total_cost, u, new_fuel_in_tank, new_fuel_in_jerry_can))

            new_total_cost = total_cost + costs[u]
            new_fuel_in_tank = fuel_in_tank
            new_fuel_in_jerry_can = 1
            if (u, new_fuel_in_tank, new_fuel_in_jerry_can) not in dist or new_total_cost < dist[
                (u, new_fuel_in_tank, new_fuel_in_jerry_can)]:
                heapq.heappush(pq, (new_total_cost, u, new_fuel_in_tank, new_fuel_in_jerry_can))

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
