import heapq
import math


def calculate_distance(point1, point2):
    """
    Обчислює евклідову відстань між двома точками на площині.

    Аргументи:
    point1, point2 (tuple[int, int]): Координати точок (x, y).

    Повертає:
    float: Евклідова відстань між точками.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def solution(n, arr) -> float:
    """
    Знаходить сумарну довжину всіх відрізків, які увійдуть у мінімальний каркас вагового графа на площині.

    Аргументи:
    n (int): Кількість точок на площині.
    arr (list[tuple[int, int]]): Список координат точок.

    Повертає:
    float: Сумарна довжина мінімального остовного дерева з точністю не менше 10^-3.
    """
    # Якщо тільки одна точка, то довжина каркаса 0.0
    if n == 1:
        return 0.0

    # Ініціалізація списку відвіданих вершин
    visited = [False] * n
    # Ініціалізація мінімальних відстаней до кожної вершини
    min_dist = [float('inf')] * n
    min_dist[0] = 0.0
    # Пріоритетна черга для зберігання мінімальних відстаней
    min_heap = [(0.0, 0)]
    total_length = 0.0

    while min_heap:
        # Отримуємо вершину з найменшою відстанню
        dist, u = heapq.heappop(min_heap)
        if visited[u]:
            continue

        # Позначаємо вершину як відвідану
        visited[u] = True
        # Додаємо відстань до загальної довжини каркаса
        total_length += dist

        for v in range(n):
            if not visited[v]:
                # Обчислюємо відстань до невідвіданої вершини
                distance = calculate_distance(arr[u], arr[v])
                if distance < min_dist[v]:
                    # Оновлюємо мінімальну відстань і додаємо у чергу
                    min_dist[v] = distance
                    heapq.heappush(min_heap, (distance, v))

    # Повертаємо загальну довжину каркаса з округленням до 5 знаків після коми
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
