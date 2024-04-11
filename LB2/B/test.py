from LB2.B.main import solution


def test_solution():
    table = [
        (
            [123, 666, 314, 666, 434],
            [
                (1, 5, 314),
                (1, 5, 578),
                (2, 4, 666),
                (4, 4, 713),
                (1, 1, 123)
            ],
            '10101'
        ),
    ]

    for p, q, r in table:
        assert solution(p, q) == r