__sensor_time_offset = {}

def transform_reading(reading):
    data_blocks = reading.split('::')
    sensor_id = None
    sensor_unknown = False
    reading_time = None
    readings = {}
    for block in data_blocks:
        key, value = block.split('=')
        if key == 'name':
            if value not in __sensor_time_offset.keys():
                sensor_unknown = True
            sensor_id = value
        elif key == 'time':
            reading_time = float(value)/1000 + __sensor_time_offset[sensor_id]
        else:
            readings[key] = float(value)

    return Reading(sensor_id, reading_time, readings = readings, sensor_unknown = sensor_unknown)


class Reading(object):

    def __init__(self, sensor_id, time, readings={}, sensor_unknown = False):
        self.sensor_id = sensor_id
        self.sensor_unknown = sensor_unknown
        self.reading_time = time
        self.readings = readings

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __repr__(self):
        return 'sensor_id={0}\nsensor_unknown={1}\nreading_time={2}\n'.format(self.sensor_id, self.sensor_unknown, self.reading_time) + self.readings.__repr__()
