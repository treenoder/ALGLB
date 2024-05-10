from Olymp.F.main import solution


def test_solution():
    table = [
        ("meter", 0),
        ("kilometer", 3),
        ("megananokilogigamicrometer", 3),
        ("millimeter^3", -9)
    ]

    for length, expected in table:
        assert solution(length) == expected
