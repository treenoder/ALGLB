# F-02: Является ли граф деревом?

def solution(m):
    n = len(m)
    num_edges = sum(sum(row) for row in m) // 2
    if num_edges != n - 1:
        return "NO"

    def dfs(v, parent):
        visited[v] = True
        for i in range(n):
            if m[v][i] == 1:
                if not visited[i]:
                    if not dfs(i, v):
                        return False
                elif i != parent:
                    return False
        return True

    visited = [False] * n
    if not dfs(0, -1):
        return "NO"
    if not all(visited):
        return "NO"

    return "YES"


def main():
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    print(solution(m))


if __name__ == '__main__':
    main()
