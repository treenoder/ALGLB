def solution(m):
    result = []
    for i in range(len(m)):
        result.append([sum(m[j][i] for j in range(len(m))), sum(m[i])])
    return result


def main():
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    res = solution(m)
    for r in res:
        print(*r)


if __name__ == '__main__':
    main()
