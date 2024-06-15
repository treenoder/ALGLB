def reverse_merge_sort(arr, start, end, di):
    if start >= end:
        return

    mid = start + (end - start) // 2

    reverse_merge_sort(arr, start, mid, di)
    reverse_merge_sort(arr, mid + 1, end, di)

    i, j = start, mid + 1
    temp = []
    while i <= mid and j <= end:
        if arr[i][di] >= arr[j][di]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= end:
        temp.append(arr[j])
        j += 1

    for i in range(len(temp)):
        arr[start + i] = temp[i]


def solution(records, queries):
    results = []

    for ci, di in queries:
        reverse_merge_sort(records, 0, len(records) - 1, di - 1)
        results.append(records[ci - 1])

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
