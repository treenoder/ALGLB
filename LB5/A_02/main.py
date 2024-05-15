def solution(costs, roads):
    ...


def main():
    input()
    costs = list(map(int, input().split()))
    m = int(input())
    roads = []
    for _ in range(m):
        roads.append(list(map(int, input().split())))
    result = solution(costs, roads)
    print(result)


if __name__ == '__main__':
    main()
