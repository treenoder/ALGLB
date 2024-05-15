import heapq


def solution(n, s, f, graph):
    # щоб починалося з 0
    s -= 1
    f -= 1

    distances = [float('inf')] * n
    distances[s] = 0
    priority_queue = [(0, s)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(n):
            if graph[current_vertex][neighbor] != -1:
                distance = current_distance + graph[current_vertex][neighbor]

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances[f] if distances[f] != float('inf') else -1


def main():
    [n, s, f] = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    result = solution(n, s, f, arr)
    print(result)


if __name__ == '__main__':
    main()
