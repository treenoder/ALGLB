from LB5.A.main import solution


def test_solution():
    table = [
        ((3, 1, 2), [
            [0, -1, 2],
            [3, 0, -1],
            [-1, 4, 0],
        ], 6),
    ]

    for (n, s, f), arr, expected in table:
        assert solution(n, s, f, arr) == expected
