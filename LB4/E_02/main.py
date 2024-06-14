# E-02: Матрица смежности взвешенного графа

def solution(m):
    """
    Знаходить ребра з максимальним та мінімальним вагами в неорієнтованому зваженому графі.

    Аргументи:
    m (list[list[int]]): Матриця суміжності графа, де m[i][j] вказує на вагу ребра між вершинами i та j.

    Повертає:
    list[list[int]]: Список ребер з максимальним та мінімальним вагами.
                     Спочатку йдуть ребра з максимальним вагами в порядку зростання вершин,
                     потім ребра з мінімальним вагами в порядку спадання вершин.
    """
    # Кількість вершин у графі
    n = len(m)

    # Список ребер з максимальною вагою
    max_edges = []

    # Список ребер з мінімальною вагою
    min_edges = []

    # Ініціалізація максимальної ваги мінімальним можливим значенням
    max_weight = float('-inf')

    # Ініціалізація мінімальної ваги максимальним можливим значенням
    min_weight = float('inf')

    for i in range(n):
        for j in range(i + 1, n):
            # Пропустити неіснуючі або не позитивні ребра
            if m[i][j] <= 0:
                continue

            # Оновлення максимальної ваги і ребер з цією вагою
            if m[i][j] > max_weight:
                max_weight = m[i][j]
                max_edges = [[i + 1, j + 1]]
            elif m[i][j] == max_weight:
                max_edges.append([i + 1, j + 1])

            # Оновлення мінімальної ваги і ребер з цією вагою
            if m[i][j] < min_weight:
                min_weight = m[i][j]
                min_edges = [[i + 1, j + 1]]
            elif m[i][j] == min_weight:
                min_edges.append([i + 1, j + 1])

    # Сортування ребер з максимальною вагою в порядку зростання вершин
    max_edges.sort(key=lambda x: [x[0], x[1]])

    # Сортування ребер з мінімальною вагою в порядку спадання вершин
    min_edges.sort(key=lambda x: [-x[0], -x[1]])

    res = max_edges + min_edges
    return res


def main():
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    res = solution(m)
    for r in res:
        print(*r)


if __name__ == '__main__':
    main()
