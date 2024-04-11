import sys
from functools import cmp_to_key


def compare(x, y):
    return int(y + x) - int(x + y)


def solution(arr):
    sorted_arr = sorted(arr, key=cmp_to_key(compare))
    return ''.join(sorted_arr)


def main():
    arr = []
    for line in sys.stdin:
        if line.strip() == '':
            break
        arr.append(line.strip())
    print(solution(arr))


if __name__ == '__main__':
    main()
