from LB5.D_02.main import solution


def test_solution():
    table = [
        (6, [
            [1, 1],
            [7, 1],
            [2, 2],
            [6, 2],
            [1, 3],
            [7, 3],
        ], 9.65685)

    ]

    for n, arr, expected in table:
        assert solution(n, arr) == expected
