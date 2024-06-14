def solution(n, edges):
    """
    Реалізація алгоритму Беллмана-Форда для пошуку найкоротших шляхів від однієї вершини до всіх інших у зваженому орієнтованому графі.

    Аргументи:
    n (int): Кількість вершин у графі.
    m (int): Кількість ребер у графі.
    edges (list[tuple[int, int, int]]): Список ребер, де кожне ребро задається трійкою (u, v, w),
                                         де u - початкова вершина, v - кінцева вершина, w - вага ребра.

    Повертає:
    list[int]: Список відстаней від вершини номер 1 до всіх інших вершин. Якщо шляху до деякої вершини не існує, відстань дорівнює 30000.
    """
    # Величезне число, що використовується для позначення нескінченної відстані
    inf = 30000
    # Ініціалізація відстаней до всіх вершин як нескінченність
    dist = [inf] * n
    # Відстань до початкової вершини (номер 1, нумерація з 0) дорівнює 0
    dist[0] = 0

    # Основний цикл алгоритму Беллмана-Форда
    for _ in range(n - 1):
        for u, v, w in edges:
            # Оновлення відстаней, якщо знайдено коротший шлях
            if dist[u - 1] != inf and dist[u - 1] + w < dist[v - 1]:
                dist[v - 1] = dist[u - 1] + w

    # Замінюємо нескінченні відстані на 30000
    dist = [d if d != inf else 30000 for d in dist]

    # Повертаємо список відстаней
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
    res = solution(n, edges)
    print(*res)


if __name__ == '__main__':
    main()
