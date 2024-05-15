from collections import defaultdict


def solution(n, arr):
    def generate_sub_numbers(num):
        sub_numbers = set()
        num_str = str(num)
        length = len(num_str)

        for mask in range(1, 1 << length):
            sub_number = ''.join([num_str[i] for i in range(length) if mask & (1 << i)])
            sub_numbers.add(int(sub_number))

        return sub_numbers

    sub_numbers_list = [generate_sub_numbers(a) for a in arr]
    dp = [defaultdict(lambda: float('inf')) for _ in range(n)]

    for sub_number in sub_numbers_list[0]:
        dp[0][sub_number] = len(str(arr[0])) - len(str(sub_number))

    for i in range(1, n):
        for sub_number in sub_numbers_list[i]:
            sub_number_length = len(str(sub_number))
            deletions = len(str(arr[i])) - sub_number_length
            for prev_sub_number in dp[i - 1]:
                if prev_sub_number <= sub_number:
                    dp[i][sub_number] = min(dp[i][sub_number], dp[i - 1][prev_sub_number] + deletions)

    min_deletions = min(dp[-1].values(), default=float('inf'))

    return min_deletions if min_deletions != float('inf') else -1


def main():
    n = int(input())
    arr = list(map(int, input()))
    result = solution(n, arr)
    print(result)


if __name__ == "__main__":
    main()
