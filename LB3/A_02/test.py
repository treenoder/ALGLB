from LB3.A_02.main import solution, Stack


def test_solution():
    table = [
        ('push', ['2'], 'ok'),
        ('back', [], '2'),
        ('pop', [], '2'),
        ('size', [], 0),
        ('pop', [], 'error'),
        ('push', ['1'], 'ok'),
        ('size', [], 1),
        ('clear', [], 'ok'),
    ]

    stack = Stack([])
    for cmd, args, expected in table:
        assert solution(stack, cmd, args) == expected
