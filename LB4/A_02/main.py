def solution(g):
    return sum(sum(row) for row in g)


def main():
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    result = solution(g)
    print(result)


if __name__ == '__main__':
    main()
