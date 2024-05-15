def is_non_decreasing(a, b):
    return int(''.join(a)) <= int(''.join(b))


def solution(n, arr):
    # Transform each number into a list of its digits
    digit_arrays = [list(str(x)) for x in arr]

    # Dynamic programming table to store the minimum removals
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            # Try every possible way to remove digits from digit_arrays[j]
            len_j = len(digit_arrays[j])
            for remove_count_j in range(len_j + 1):
                reduced_j = digit_arrays[j][remove_count_j:]

                # Try every possible way to remove digits from digit_arrays[i]
                len_i = len(digit_arrays[i])
                for remove_count_i in range(len_i + 1):
                    reduced_i = digit_arrays[i][remove_count_i:]

                    if reduced_j and reduced_i and is_non_decreasing(reduced_j, reduced_i):
                        dp[i] = min(dp[i], dp[j] + remove_count_j + remove_count_i)

    return dp[-1] if dp[-1] != float('inf') else -1


def main():
    n = int(input().strip())
    arr = [int(input().strip()) for _ in range(n)]
    result = solution(n, arr)
    print(result)


if __name__ == "__main__":
    main()
