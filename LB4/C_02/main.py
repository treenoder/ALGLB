def solution(m):
    """
    Обчислює півступені заходу та півступені виходу для кожної вершини орієнтованого графа, заданого матрицею суміжності.

    Півступінь заходу обчислюється як сума елементів у стовпці i матриці m.
    Півступінь виходу обчислюється як сума елементів у рядку i матриці m.

    Параметри:
    m (list of list of int): Матриця суміжності орієнтованого графа, де m[i][j] = 1, якщо існує ребро з вершини i в вершину j, і m[i][j] = 0 в іншому випадку.

    Повертає:
    list of list of int: Список пар чисел, де кожна пара містить півступінь заходу та півступінь виходу для відповідної вершини.
    """
    result = []
    for i in range(len(m)):
        # Півступінь заходу - кількість ребер, які входять у вершину i
        in_degree = sum(m[j][i] for j in range(len(m)))
        # Півступінь виходу - кількість ребер, які виходять з вершини i
        out_degree = sum(m[i])
        result.append([in_degree, out_degree])
    return result


def main():
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    res = solution(m)
    for r in res:
        print(*r)


if __name__ == '__main__':
    main()
