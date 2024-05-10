from Olymp.A.main import solution


def test_solution():
    table = [
        (1, 1, 1, 0),
        (9, 9, 10, 1),
    ]

    for A, B, C, expected in table:
        assert solution(A, B, C) == expected
