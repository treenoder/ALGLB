from Olymp.B.main import solution


def test_solution():
    table = [
        (1, 198),
        (2, 297),
    ]

    for x, expected in table:
        assert solution(x) == expected
