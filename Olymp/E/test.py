from Olymp.E.main import solution


def test_solution():
    table = [
        (5, 180, [40, 60, 80, 50], 70),
        (3, 100, [100, 100], 0),
        (5, 200, [0, 0, 99, 99], -1),
        (10, 480, [59, 98, 88, 54, 70, 24, 8, 94, 46], 45)
    ]

    for _, s, arr, expected in table:
        assert solution(s, arr) == expected
