def solution(n, m):
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[j][i]:
                return 'NO'
    if sum(m[i][i] for i in range(n)) != 0:
        return 'NO'
    return 'YES'


def main():
    n = int(input())
    for _ in range(n):
        s = int(input())
        m = [list(map(int, input().split())) for _ in range(s)]
        print(solution(s, m))


if __name__ == '__main__':
    main()
