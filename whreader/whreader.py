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


class Reading(object):

    def __init__(self, name, time, readings={}):
        self.device_name = name
        self.reading_time = time
        self.readings = readings

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __repr__(self):
        return 'device_name={}\nreading_time={}\n'.format(self.device_name, self.reading_time) + self.readings.__repr__()
