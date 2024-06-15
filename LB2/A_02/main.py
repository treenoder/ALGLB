def is_possible(distance, stalls, k):
    count = 1
    last_position = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= distance:
            count += 1
            last_position = stalls[i]
            if count == k:
                return True
    return False


def solution(arr, k):
    left = 0
    right = arr[-1] - arr[0]
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid, arr, k):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


def main():
    k = int(input().split()[1])
    arr = list(map(int, input().split()))
    print(solution(arr, k))


if __name__ == '__main__':
    main()
