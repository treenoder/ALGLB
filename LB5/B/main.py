def solution(n, dist):
    """
    Реалізація алгоритму Флойда-Воршелла для знаходження найкоротших шляхів між усіма парами вершин у зваженому орієнтованому графі.

    Аргументи:
    n (int): Кількість вершин у графі.
    arr (list[list[int]]): Матриця суміжності графа, де arr[i][j] означає вагу ребра з вершини i до вершини j. Значення на головній діагоналі дорівнюють нулю.

    Повертає:
    list[list[int]]: Матриця найкоротших відстаней між парами вершин.
    """
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Оновлюємо найкоротшу відстань між вершинами i та j через вершину k
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Повертаємо матрицю найкоротших відстаней
    return dist


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

    result = solution(n, arr)
    for i in range(n):
        print(' '.join(map(str, result[i])))


if __name__ == '__main__':
    main()
