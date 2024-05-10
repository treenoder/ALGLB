def solution(a, b, c) -> tuple[int, int]:
    diff1 = abs(b - a)
    diff2 = abs(c - b)
    d = min(diff1, diff2) * (-1 if b < a else 1)
    if diff1 < diff2:
        return b + d, 3
    elif diff1 > diff2:
        return a + d, 2
    else:
        return c + d, 4


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    result = solution(a, b, c)
    print(result[0])
    print(result[1])


if __name__ == '__main__':
    main()
