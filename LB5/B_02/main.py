def solution(n, arr):
    """
    Реалізація алгоритму для знаходження транзитивного замикання орієнтованого графа.

    Транзитивне замикання графа G - це граф, у якому є ребро (i, j), якщо у вихідному графі існує шлях з i в j.

    Аргументи:
    n (int): Кількість вершин у графі.
    arr (list[list[int]]): Матриця суміжності графа, де arr[i][j] = 1, якщо є ребро з вершини i до вершини j, і 0 - якщо ні.

    Повертає:
    list[list[int]]: Матриця суміжності транзитивного замикання графа.
    """
    # Ініціалізація матриці замикання, копіюючи початкову матрицю суміжності
    closure = [[arr[i][j] for j in range(n)] for i in range(n)]

    # Основний цикл алгоритму для знаходження транзитивного замикання
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Оновлюємо значення замикання для вершини (i, j) через вершину k
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    # Повертаємо матрицю замикання
    return closure


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
