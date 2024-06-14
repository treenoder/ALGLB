def solution(n, arr):
    """
    Визначає, чи існує в орієнтованому графі цикл від'ємної ваги за допомогою алгоритму Беллмана-Форда. Якщо такий цикл існує, виводить його.

    Аргументи:
    n (int): Кількість вершин у графі.
    arr (list[list[int]]): Матриця суміжності графа, де arr[u][v] показує вагу ребра від вершини u до вершини v,
                           або 100000, якщо ребра немає.

    Повертає:
    tuple: Повертає кортеж (довжина циклу, список вершин у циклі) або (0, []), якщо циклу не існує.
    """

    def find_negative_cycle():
        # Ініціалізація відстаней до нескінченності
        dist = [float('inf')] * n
        # Попередники для відновлення шляху
        pred = [-1] * n

        # Пробуємо кожну вершину як стартову
        for src in range(n):
            # Відстань від стартової вершини до самої себе рівна 0
            dist[src] = 0
            # Робимо n-1 ітерації
            for _ in range(n - 1):
                for u in range(n):
                    for v in range(n):
                        if arr[u][v] != 100000 and dist[u] + arr[u][v] < dist[v]:
                            dist[v] = dist[u] + arr[u][v]
                            pred[v] = u

            # Перевірка на наявність циклу від'ємного ваги
            for u in range(n):
                for v in range(n):
                    if arr[u][v] != 100000 and dist[u] + arr[u][v] < dist[v]:
                        cycle = []
                        x = v
                        # Відновлюємо цикл
                        for _ in range(n):
                            x = pred[x]

                        cycle_start = x
                        # Зберігаємо цикл до його повторення
                        while True:
                            cycle.append(cycle_start + 1)
                            cycle_start = pred[cycle_start]
                            if cycle_start + 1 in cycle:
                                cycle.append(cycle_start + 1)
                                break

                        # Перевертаємо, щоб цикл був від початку до кінця
                        cycle.reverse()
                        # Отримуємо цикл без повторень
                        cycle = cycle[cycle.index(cycle_start + 1):-1]

                        return len(cycle), cycle

        # Якщо циклу не знайдено
        return 0, []

    return find_negative_cycle()


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    arr = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index + n]))
        arr.append(row)
        index += n

    count, verts = solution(n, arr)
    if not count:
        print('NO')
        return
    print('YES')
    print(count)
    print(' '.join(map(str, verts)))


if __name__ == '__main__':
    main()
