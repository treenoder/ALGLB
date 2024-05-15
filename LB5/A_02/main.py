def solution(n, costs, roads):
    ...


def main():
    n = int(input())
    costs = list(map(int, input().split()))
    m = int(input())
    roads = [list(map(int, input().split())) for _ in range(m)]
    result = solution(n, costs, roads)
    print(result)


if __name__ == '__main__':
    main()
