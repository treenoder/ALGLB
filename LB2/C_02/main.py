def calculate_weights(N, m1, mN, d):
    l, r = -1000, 1000
    while r - l > 1e-7:
        m2 = (l + r) / 2
        weights = [m1, m2]
        for i in range(2, N):
            mi_plus1 = 2 * weights[-1] - weights[-2] - 2 * d
            weights.append(mi_plus1)
        if abs(weights[-1] - mN) < 1e-7:
            return weights
        if weights[-1] > mN:
            r = m2
        else:
            l = m2
    return weights


def solution(N, m1, mN, d, I, J, K):
    I, J, K = int(I), int(J), int(K)
    weights = calculate_weights(int(N), m1, mN, d)
    weight = weights[I - 1] + weights[J - 1] + weights[K - 1]
    return f"{weight:.4f}"


def main():
    N, m1, mN, d, I, J, K = map(float, input().split())
    print(solution(N, m1, mN, d, I, J, K))


if __name__ == '__main__':
    main()
