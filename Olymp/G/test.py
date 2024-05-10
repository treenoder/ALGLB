from Olymp.G.main import solution


def test_solution():
    table = [
        ("123+45+67", 12412),
        ("10-20-30", 990),
    ]

    for ex, expected in table:
        assert solution(ex) == expected
