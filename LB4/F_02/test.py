from LB4.F_02.main import solution


def test_solution():
    table = [
        ([
             [0, 1, 1, 0, 0, 0],
             [1, 0, 1, 0, 0, 0],
             [1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0],
         ], 'NO'),
        ([
             [0, 1, 0],
             [1, 0, 1],
             [0, 1, 0],
         ], 'YES'),
    ]

    for m, expected in table:
        assert solution(m) == expected
