from LB4.B_02.main import solution


def test_solution():
    table = [
        ([
             [0, 1, 1],
             [1, 0, 1],
             [1, 1, 0]
         ], 'YES'),
        ([
             [0, 1, 0],
             [1, 0, 1],
             [1, 1, 0]
         ], 'NO'),
        ([
             [0, 1, 0],
             [1, 1, 1],
             [0, 1, 0]
         ], 'NO'),
    ]

    for m, expected in table:
        assert solution(len(m), m) == expected
