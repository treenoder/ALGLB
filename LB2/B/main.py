def solution(p, q):
    passengers_count = {}
    for passengers in p:
        if passengers not in passengers_count:
            passengers_count[passengers] = 0
        passengers_count[passengers] += 1

    results = []
    for l, r, x in q:
        count = 0
        for city_number in range(l - 1, r):
            if p[city_number] == x:
                count += 1
        results.append('1' if count > 0 else '0')

    return ''.join(results)


def main():
    input()
    p = list(map(int, input().split()))
    k = int(input())
    q = [list(map(int, input().split())) for _ in range(k)]
    print(solution(p, q))


if __name__ == '__main__':
    main()
