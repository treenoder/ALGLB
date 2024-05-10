from Olymp.D.main import solution


def test_solution():
    table = [
        (5000, 10, 2500, 8, 4, 6),
        (5027, 56, 1813, 9, 8, 0),
    ]

    for l, t, k, v1, v2, expected in table:
        assert solution(l, t, k, v1, v2) == expected
