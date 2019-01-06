__sensor_devices = {}


def transform_reading(reading):
    data_blocks = reading.split('::')
    device_name = None
    reading_time = None
    readings = {}
    for block in data_blocks:
        key, value = block.split('=')
        if key == 'name':
            device_name = value
        elif key == 'time':
            # TODO Add checking whether device supplying reading is registered and then applying any needed offset
            reading_time = float(value)
        else:
            readings[key] = float(value)

    return Reading(device_name, reading_time, readings)


def register_sensor(device):
    id = device.id
    if id in __sensor_devices.keys():
        raise Exception('Device with ID {} already registered'.format(id))
    __sensor_devices[id] = device


class Reading(object):

    def __init__(self, dev_id, time, readings={}):
        self.device_id = dev_id
        self.reading_time = time
        self.readings = readings

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __repr__(self):
        return 'device_id={}\nreading_time={}\n'.format(self.device_id, self.reading_time) + self.readings.__repr__()


class SensorDevice(object):

    def __init__(self, id, time_offset=0):
        self.id = id
        self.time_offset = time_offset

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __repr__(self):
        return 'device_id={0}\ntime_offset={1}'.format(self.id, self.time_offset)