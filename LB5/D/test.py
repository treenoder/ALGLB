from LB5.D.main import solution


def test_solution():
    table = [
        (3, 3, [
            [1, 2, 2],
            [2, 3, 8],
            [1, 3, 10],
        ], (10, [1, 2])),
        (3, 1, [
            [1, 2, 2],
        ], (-1, []))
    ]

    for n, m, arr, expected in table:
        assert solution(n, m, arr) == expected
