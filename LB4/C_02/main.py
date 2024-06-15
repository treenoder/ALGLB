def solution(m):
    result = []
    for i in range(len(m)):
        in_degree = sum(m[j][i] for j in range(len(m)))
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
