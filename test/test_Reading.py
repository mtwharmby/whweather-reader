from whwreader.whwreader import Reading


def test_repr():
    expected = 'device_name=boris\nreading_time=2134457\n{}'.format({'temp': 25.5, 'humid': 56.8}.__repr__())

    string_form = Reading('boris', 2134457, readings={'temp': 25.5, 'humid': 56.8}).__repr__()
    assert string_form == expected


def test_equality():
    first = Reading('boris', 2134457, readings={'temp': 25.5, 'humid': 56.8})
    second = Reading('boris', 2134457, readings={'temp': 25.5, 'humid': 56.8})
    third = Reading('hugo', 238357, readings={'temp': 285.2, 'humid': 85.3})
    fourth = Reading('boris', 2134457, readings={'temp': 28.5, 'humid': 57.8})

    assert first == second
    assert first != third
    assert first != fourth