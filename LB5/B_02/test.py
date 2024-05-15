from LB5.B_02.main import solution


def test_solution():
    table = [
        (4, [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [0, 0, 1, 1],
        ], [
             [1, 1, 1, 0],
             [1, 1, 1, 0],
             [1, 1, 1, 0],
             [1, 1, 1, 1],
         ])
    ]

    for n, arr, expected in table:
        assert solution(n, arr) == expected
