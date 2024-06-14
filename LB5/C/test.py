from LB5.C.main import solution


def test_solution():
    table = [
        (4, 5, [
            [1, 2, 10],
            [2, 3, 10],
            [1, 3, 100],
            [3, 1, -10],
            [2, 3, 1],
        ], [0, 10, 11, 30000])
    ]

    for n, m, arr, expected in table:
        assert solution(n, arr) == expected
