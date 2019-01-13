import serial

from whwreader import whwreader
from whwreader.sensor_readers import SerialSensorReader


def test_sensor_read(monkeypatch):
    def mock_serial_readline():
        return "name=boris::time=2134457::temp=25.5::humid=56.8".encode(encoding='utf_8')
    def mock_reading():
        return whwreader.Reading('boris', 2134.457, {'temp': 25.5, 'humid': 56.8}, sensor_unknown=False)

    monkeypatch.setattr(serial.Serial, 'readline', mock_serial_readline)
    monkeypatch.setattr(whwreader, 'transform_reading', mock_reading)

    reading_list = []

    ser_reader = SerialSensorReader('COM9', 9600, reading_list)
    ser_reader.do_sensor_read()

    assert len(reading_list) == 1
    assert reading_list[0] == mock_reading()