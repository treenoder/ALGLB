# E-02: Матрица смежности взвешенного графа
def solution(m):
    n = len(m)
    max_edges = []
    min_edges = []
    max_weight = 0
    min_weight = 0

    for i in range(n):
        for j in range(i + 1, n):
            if m[i][j] <= 0:
                continue
            if m[i][j] > max_weight:
                max_weight = m[i][j]
                max_edges = [[i + 1, j + 1]]
            elif m[i][j] == max_weight:
                max_edges.append([i + 1, j + 1])
            if m[i][j] < min_weight or min_weight == 0:
                min_weight = m[i][j]
                min_edges = [[i + 1, j + 1]]
            elif m[i][j] == min_weight:
                min_edges.append([i + 1, j + 1])

    max_edges.sort(key=lambda x: x[1])
    min_edges.sort(key=lambda x: x[1], reverse=True)

    return max_edges + min_edges


def main():
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    res = solution(m)
    for r in res:
        print(*r)


if __name__ == '__main__':
    main()
