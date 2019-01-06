import pytest

import whwreader.whwreader as whwreader
from whwreader.whwreader import Reading, SensorDevice


def test_transform():
    sensor_reading = "name=boris::time=2134457::temp=25.5::humid=56.8"
    expected = Reading('boris', 2134457.0, readings={'temp': 25.5, 'humid': 56.8})

    structured_read = whwreader.transform_reading(sensor_reading)
    assert structured_read == expected

    #TODO Add test of updating time


def test_device_registration():
    test_sensor_rpi1 = SensorDevice('RPi1')
    test_sensor_ard1 = SensorDevice('arduino1', time_offset=1546804623.6360931)

    assert len(whwreader.__sensor_devices) == 0
    whwreader.register_sensor(test_sensor_rpi1)
    assert len(whwreader.__sensor_devices) == 1
    assert whwreader.__sensor_devices['RPi1'] == test_sensor_rpi1

    with pytest.raises(Exception):
        #Shouldn't be able to register same sensor (ID) twice
        whwreader.register_sensor(test_sensor_rpi1)

    whwreader.register_sensor(test_sensor_ard1)
    assert len(whwreader.__sensor_devices) == 2
    assert whwreader.__sensor_devices['arduino1'] == test_sensor_ard1
    