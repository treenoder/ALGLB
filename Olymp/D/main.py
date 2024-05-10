import math


def solution(l, t, k, v1, v2) -> int:
    fast_time = k / (v1 * 60)
    slow_time = (l - k) / (v2 * 60)
    time = math.ceil(fast_time + slow_time)
    if time > t:
        return time - t
    return 0


def main():
    [l, t] = list(map(int, input().split()))
    k = int(input())
    [v1, v2] = list(map(int, input().split()))
    result = solution(l, t, k, v1, v2)
    if result:
        print(f"Algorithmius will be {result} minutes late")
    else:
        print("The pizza will be delivered on time")


if __name__ == '__main__':
    main()
