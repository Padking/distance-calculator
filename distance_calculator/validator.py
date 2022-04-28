def validate(*args):
    from_city = args[0]
    to_city = args[1]

    assert 0 <= from_city < 50, 'Значение ключа `from_city` д.б. [0, 50)'
    assert 0 <= to_city < 50, 'Значение ключа `to_city` д.б. [0, 50)'
