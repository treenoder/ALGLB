def solution(v, e, m):
    g = [[] for _ in range(v)]
    for i, j in m:
        g[i - 1].append(j - 1)
        g[j - 1].append(i - 1)

    for i in range(v):
        for j in range(v):
            if i == j:
                continue
            if j not in g[i]:
                return 'NO'
    return 'YES'


def main():
    n = int(input())
    for _ in range(n):
        v, e = map(int, input().split())
        m = [list(map(int, input().split())) for _ in range(e)]
        print(solution(v, e, m))


if __name__ == '__main__':
    main()
