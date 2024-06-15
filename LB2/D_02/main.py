def solution(records, queries):
    results = []

    for ci, di in queries:
        sorted_records = sorted(records, key=lambda x: x[di-1], reverse=True)
        results.append(sorted_records[ci-1])

    return results


def main():
    N, M = map(int, input().split())

    records = [list(map(int, input().split())) for _ in range(N)]

    K = int(input())

    queries = [tuple(map(int, input().split())) for _ in range(K)]

    results = solution(records, queries)
    for result in results:
        print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
