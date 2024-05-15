from LB5.B.main import solution


def test_solution():
    table = [
        (4, [
            [0, 5, 9, 100],
            [100, 0, 2, 8],
            [100, 100, 0, 7],
            [4, 100, 100, 0],
        ], 2)
    ]

    for n, arr, expected in table:
        assert solution(n, arr) == expected
