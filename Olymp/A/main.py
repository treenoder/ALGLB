def solution(A, B, C):
    B += C // 10
    A += B // 10

    return A // 10


def main():
    A = int(input())
    B = int(input())
    C = int(input())
    result = solution(A, B, C)
    print(result)


if __name__ == '__main__':
    main()
