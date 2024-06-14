class UnionFind:
    """
    Клас Union-Find для об'єднання та знаходження з представником наборів.

    Аргументи:
    n (int): Кількість елементів.
    """

    def __init__(self, n):
        self.parent = list(range(n))
        # Ініціалізація рангу для кожного елемента
        self.rank = [0] * n

    def find(self, u):
        """
        Знаходить представника набору, до якого належить елемент.

        Аргументи:
        u (int): Елемент, для якого потрібно знайти представника.

        Повертає:
        int: Представник набору.
        """
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        """
        Об'єднує два набори, до яких належать елементи u та v.

        Аргументи:
        u (int): Елемент першого набору.
        v (int): Елемент другого набору.
        """
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def solution(n, arr) -> tuple[int, list[int]]:
    """
    Реалізація алгоритму Крускала для знаходження мінімального остовного дерева у зваженому неорієнтованому графі.

    Мінімальне остовне дерево - це підграф зваженого графа, який є деревом, містить всі вершини графа і має мінімальну можливу вагу.

    Алгоритм починається з сортування всіх ребер графа за зростанням їх ваги.
    Після сортування ребра додаються до мінімального остовного дерева в порядку їх ваги, якщо вони не утворюють цикл з вже включеними в дерево ребрами.
    Для перевірки утворення циклів і об'єднання підмножин вершин використовується структура даних UnionFind.

    Аргументи:
    n (int): Кількість вершин у графі.
    m (int): Кількість ребер у графі.
    arr (list[tuple[int, int, int]]): Список ребер, де кожне ребро задається трійкою (u, v, w),
                                       де u і v - вершини, що з'єднуються ребром, w - вага ребра.

    Повертає:
    tuple: Кортеж, що містить вагу мінімального остовного дерева і список індексів ребер, що входять до нього,
           або -1 і порожній список, якщо остовне дерево не існує.
    """
    # Сортуємо ребра за вагою
    edges = sorted((w, u - 1, v - 1, i + 1) for i, (u, v, w) in enumerate(arr))
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []

    for w, u, v, index in edges:
        # Додаємо ребро до остовного дерева, якщо воно не утворює цикл
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += w
            mst_edges.append(index)
        # Якщо ми вже додали n - 1 ребро, виходимо з циклу
        if len(mst_edges) == n - 1:
            break

    # Якщо не вдалося побудувати остовне дерево, повертаємо -1 і порожній список
    if len(mst_edges) != n - 1:
        return -1, []

    # Повертаємо вагу мінімального остовного дерева і список ребер
    return mst_weight, mst_edges


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    m = int(data[1])
    arr = []

    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        arr.append((u, v, w))
        index += 3

    count, edges = solution(n, arr)
    if count == -1:
        print('-1')
        return
    print(count)
    for edge in edges:
        print(edge)


if __name__ == '__main__':
    main()
