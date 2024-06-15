import heapq
import math


def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def solution(n, arr) -> float:
    """
    Знаходить сумарну довжину всіх відрізків, які увійдуть у мінімальний каркас вагового графа на площині.

    Застосовується алгоритм Пріма.
    Алгоритм починає з довільної вершини і поступово розширює MST, додаючи до нього вершини, найближчі до вже включених у дерево.
    Кожного разу до мінімального остовного дерева додається найменше ребро, яке з'єднує вже включені в дерево вершини з тими, що ще не включені.
    Використовується пріоритетна черга для ефективного вибору наступного ребра з найменшою вагою.

    Аргументи:
    n (int): Кількість точок на площині.
    arr (list[tuple[int, int]]): Список координат точок.

    Повертає:
    float: Сумарна довжина мінімального остовного дерева з точністю не менше 10^-3.
    """
    # Якщо тільки одна точка, то довжина каркаса 0.0
    if n == 1:
        return 0.0

    visited = [False] * n
    min_dist = [float('inf')] * n
    min_dist[0] = 0.0
    min_heap = [(0.0, 0)]
    total_length = 0.0

    while min_heap:
        dist, u = heapq.heappop(min_heap)
        if visited[u]:
            continue

        visited[u] = True
        total_length += dist

        for v in range(n):
            if not visited[v]:
                distance = calculate_distance(arr[u], arr[v])
                if distance < min_dist[v]:
                    min_dist[v] = distance
                    heapq.heappush(min_heap, (distance, v))

    return round(total_length, 5)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    arr = []
    for i in range(n):
        x = int(data[2 * i + 1])
        y = int(data[2 * i + 2])
        arr.append((x, y))

    total_length = solution(n, arr)
    print(total_length)


if __name__ == '__main__':
    main()
