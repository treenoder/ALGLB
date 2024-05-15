def is_non_decreasing(sequence):
    return all(sequence[i] <= sequence[i + 1] for i in range(len(sequence) - 1))


def backtrack(numbers, index, current_sequence, min_removals, current_removals):
    if index == len(numbers):
        if is_non_decreasing(current_sequence):
            min_removals[0] = min(min_removals[0], current_removals)
        return

    number_str = numbers[index]
    for i in range(len(number_str) + 1):
        new_sequence = current_sequence[:]
        if i < len(number_str):
            new_number = number_str[:i] + number_str[i + 1:]
            if not new_number:
                continue
            new_number = int(new_number)
        else:
            new_number = int(number_str)
        new_sequence.append(new_number)
        backtrack(numbers, index + 1, new_sequence, min_removals,
                  current_removals + (len(number_str) - len(str(new_number))))
        new_sequence.pop()


def solution(n, arr):
    if n == 1:
        return 0

    numbers = [str(num) for num in arr]
    min_removals = [float('inf')]
    backtrack(numbers, 0, [], min_removals, 0)

    return min_removals[0] if min_removals[0] != float('inf') else -1


# def solution(n, arr) -> int:
#     ...


def main():
    n = int(input())
    arr = list(map(int, input()))
    result = solution(n, arr)
    print(result)


if __name__ == "__main__":
    main()
