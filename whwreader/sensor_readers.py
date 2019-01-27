from abc import ABC, abstractmethod


class SensorReader(ABC):

    @abstractmethod
    def initialise_sensor(self):
        '''Adds ID of device to list of sensor readers along with any other config'''

    @abstractmethod
    def do_sensor_read(self):
        '''On receipt of sensor reading, transforms it and writes to the db write list'''


class SerialSensorReader(SensorReader):
    pass
