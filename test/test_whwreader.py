from whwreader.whwreader import transform_reading, Reading


def test_transform():
    sensor_reading = "name=boris::time=2134457::temp=25.5::humid=56.8"
    expected = Reading('boris', 2134457.0, readings={'temp': 25.5, 'humid': 56.8})

    structured_read = transform_reading(sensor_reading)
    assert structured_read == expected


def test_Reading_repr():
    expected = 'device_name=boris\nreading_time=2134457\n{}'.format({'temp': 25.5, 'humid': 56.8}.__repr__())

    string_form = Reading('boris', 2134457, readings={'temp': 25.5, 'humid': 56.8}).__repr__()
    assert string_form == expected
