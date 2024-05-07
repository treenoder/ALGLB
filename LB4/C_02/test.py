from LB4.C_02.main import solution


def test_solution():
    table = [
        ([
             [0, 1, 0, 1],
             [1, 0, 1, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1],
         ], [
             [2, 2],
             [3, 3],
             [2, 1],
             [3, 4]
         ]),
    ]

    for m, expected in table:
        assert solution(m) == expected
