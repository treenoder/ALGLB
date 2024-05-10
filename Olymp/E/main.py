def solution(s, arr: list) -> int:
    original_total = sum(arr)
    mn = min(arr)
    mx = max(arr)
    for last in range(101):
        total = original_total + last
        new_min = min(mn, last)
        new_max = max(mx, last)
        final = total - new_min - new_max
        if final >= s:
            return last
    return -1


def main():
    [_, s] = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = solution(s, arr)
    print(result)


if __name__ == '__main__':
    main()
