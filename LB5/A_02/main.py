def solution(narr, marr):
    ...


def main():
    input()
    narr = list(map(int, input().split()))
    m = int(input())
    marr = []
    for _ in range(m):
        marr.append(list(map(int, input().split())))
    result = solution(narr, marr)
    print(result)


if __name__ == '__main__':
    main()
