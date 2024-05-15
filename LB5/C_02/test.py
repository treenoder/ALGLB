from LB5.C_02.main import solution


def test_solution():
    table = [
        (2, [
            [0, -1],
            [-1, 0]
        ], (2, [2, 1]))
    ]

    for n, arr, expected in table:
        assert solution(n, arr) == expected
