from LB2.E_02.main import solution


def test_solution():
    assert solution(['2', '20', '004', '66']) == '66220004'
    assert solution(['3']) == '3'

