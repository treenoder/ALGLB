def solution(n, s, arr: list) -> int:
    original_total = sum(arr)
    mn = min(arr)
    mx = max(arr)
    arr.remove(mn)
    arr.remove(mx)
    total = sum(arr)
    target = s - total
    if target > 100:
        return -1
    if mn == mx == 100:
        return 0

    return target


def main():
    [n, s] = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = solution(n, s, arr)
    print(result)


if __name__ == '__main__':
    main()
