from whreader.whreader import transform_reading, Reading


def test_transform():
    sensor_reading = "name=boris::time=2134457::temp=25.5::humid=56.8"
    expected = Reading('boris', 2134457, readings={'temp': 25.5, 'humid': 56.8})

    structured_read = transform_reading(sensor_reading)
    assert structured_read == expected
