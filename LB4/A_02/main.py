"""
Матриця суміжності — це спосіб представлення графа у вигляді двовимірної таблиці (матриці), де рядки і стовпці відповідають вершинам графа.
"""


def solution(g):
    """
    Обчислює кількість ребер в орієнтованому графі, заданому матрицею суміжності.

    Матриця суміжності - це двовимірний список, де g[i][j] = 1, якщо існує ребро з вершини i в вершину j, і g[i][j] = 0 в іншому випадку.

    Параметри:
    g (list of list of int): Матриця суміжності орієнтованого графа, де g[i][j] = 1, якщо існує ребро з вершини i в вершину j, і g[i][j] = 0 в іншому випадку.

    Повертає:
    int: Кількість ребер в графі.
    """
    return sum(sum(row) for row in g)


def main():
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    result = solution(g)
    print(result)


if __name__ == '__main__':
    main()
