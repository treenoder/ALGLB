import heapq


def solution(n, s, f, graph):
    """
    Реалізація алгоритму Дейкстри для пошуку найкоротшого шляху в орієнтованому зваженому графі.

    Аргументи:
    n (int): Кількість вершин у графі.
    s (int): Початкова вершина (нумерація з 1).
    f (int): Кінцева вершина (нумерація з 1).
    graph (list[list[int]]): Матриця суміжності графа, де graph[i][j] означає вагу ребра від вершини i до вершини j. -1 означає відсутність ребра.

    Повертає:
    int: Найкоротша відстань від вершини s до вершини f. Повертає -1, якщо шляху не існує.
    """
    # Перетворення нумерації вершин на 0-індексовану
    s -= 1
    f -= 1

    # Ініціалізація відстаней до всіх вершин як безкінечність, крім стартової вершини
    distances = [float('inf')] * n
    distances[s] = 0

    # Пріоритетна черга для зберігання поточної найкоротшої відстані до вершини
    priority_queue = [(0, s)]

    while priority_queue:
        # Витягуємо вершину з мінімальною відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо знайдена відстань більша за поточну, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Проходимося по всіх сусідах поточної вершини
        for neighbor in range(n):
            if graph[current_vertex][neighbor] != -1:
                distance = current_distance + graph[current_vertex][neighbor]

                # Якщо знайдена менша відстань, оновлюємо її
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    # Повертаємо найкоротшу відстань до кінцевої вершини або -1, якщо шлях не знайдено
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
