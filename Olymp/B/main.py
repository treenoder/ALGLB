def solution(first_x: int) -> int:
    for diff in range(1, 10):
        x = 99 * diff
        if str(x)[0] == str(first_x):
            return x


def main():
    first_x = int(input())
    result = solution(first_x)
    print(result)


if __name__ == '__main__':
    main()
