import pytest

import whwreader.whwreader as whwreader
from whwreader.whwreader import Reading


def test_transform():
    #Preamble
    whwreader.__sensor_time_offset['boris'] = 0
    whwreader.__sensor_time_offset['charles'] = 1546804623.6360931

    sensor_reading = "name=boris::time=2134457::temp=25.5::humid=56.8"
    #expected = Reading('boris', 2134.457, readings={'temp': 25.5, 'humid': 56.8}, sensor_unknown=False)
    expected = Reading('boris', 2134.457, {'temp': 25.5, 'humid': 56.8}, sensor_unknown=False)
    structured_read = whwreader.transform_reading(sensor_reading)
    assert structured_read == expected

    #Now test against an offset time. N.B. Expecting time in ms
    sensor_reading_2 = "name=charles::time=600::temp=32.5::humid=22.6"
    expected_2 = Reading('charles', 1546804623.6360931 + 0.6, readings={'temp': 32.5, 'humid': 22.6})
    structured_read = whwreader.transform_reading(sensor_reading_2)
    assert structured_read == expected_2
