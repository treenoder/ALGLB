# F-02: Является ли граф деревом?

def solution(m):
    """
    Перевіряє, чи є неорієнтований граф деревом на основі його матриці суміжності.

    Граф вважається деревом, якщо він є зв'язним і ациклічним, та містить рівно (N - 1) ребро для N вершин.


    Аргументи:
    m (list[list[int]]): Матриця суміжності графа, де m[i][j] = 1 вказує на наявність ребра між вершинами i та j,
                         а m[i][j] = 0 - на його відсутність.

    Повертає:
    str: "YES" якщо граф є деревом, "NO" якщо не є.
    """
    # Кількість вершин у графі
    n = len(m)

    # Підрахунок кількості ребер
    num_edges = sum(sum(row) for row in m) // 2

    # Дерево має містити рівно n-1 ребро
    if num_edges != n - 1:
        return "NO"

    # Функція для глибокого пошуку (DFS)
    def dfs(v, parent):
        """
        Часова O(V + E), де V - кількість вершин, а E - кількість ребер у графі.
        """
        visited[v] = True
        for i in range(n):
            if m[v][i] == 1:
                if not visited[i]:
                    if not dfs(i, v):
                        return False
                elif i != parent:
                    return False
        return True

    # Масив для відстеження відвіданих вершин
    visited = [False] * n

    # Запуск DFS з першої вершини
    if not dfs(0, -1):
        return "NO"

    # Перевірка на зв'язність графа (чи існує шлях між будь-якою парою вершин)
    if not all(visited):
        return "NO"

    return "YES"


def main():
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    print(solution(m))


if __name__ == '__main__':
    main()
