import sys


def right_binary_search(arr, target):
    left, right = 0, len(arr) - 1

    if arr[right] < target or arr[left] > target:
        return -1

    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            result = mid
            left = mid + 1

    return result


def solution(arr, idx):
    results = []
    for id in idx:
        res = right_binary_search(arr, id) + 1
        results.append(res)
    return results


def main():
    input()
    arr = list(map(int, input().split()))
    idx = []
    for i, line in enumerate(sys.stdin):
        idx.append(int(line))
    result = solution(arr, idx)
    for r in result:
        print(r)


if __name__ == '__main__':
    main()
