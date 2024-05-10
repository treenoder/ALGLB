from Olymp.C.main import solution


def test_solution():
    table = [
        # (1, 5, 7, (3, 2)),
        # (5, 10, 15, (20, 4)),
        (41, 31, 11, (21, 3)),
        # (10, 17, 24, (3, 1)),
    ]

    for a, b, c, expected in table:
        assert solution(a, b, c) == expected
