class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
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


def solution(n, m, arr) -> tuple[int, list[int]]:
    edges = sorted((w, u - 1, v - 1, i + 1) for i, (u, v, w) in enumerate(arr))
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []

    for w, u, v, index in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += w
            mst_edges.append(index)
        if len(mst_edges) == n - 1:
            break

    if len(mst_edges) != n - 1:
        return -1, []

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

    count, edges = solution(n, m, arr)
    if count == -1:
        print('-1')
        return
    print(count)
    for edge in edges:
        print(edge)


if __name__ == '__main__':
    main()
