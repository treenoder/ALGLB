def solution(n: int, arr: list[int]) -> int:
    arr.sort()
    minimal_difference = float('inf')

    for host_index in range(n):
        paired_sums = []
        left, right = 0, n - 1
        while left < right:
            if left == host_index:
                left += 1
            elif right == host_index:
                right -= 1
            else:
                paired_sums.append(arr[left] + arr[right])
                left += 1
                right -= 1

        if paired_sums:
            current_difference = max(paired_sums) - min(paired_sums)
            minimal_difference = min(minimal_difference, current_difference)

    return minimal_difference


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = solution(n, arr)
    print(result)


if __name__ == "__main__":
    main()
