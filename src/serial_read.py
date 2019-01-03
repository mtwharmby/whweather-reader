import serial


class SerialLink(serial.Serial):

    def extract_time_temp(self):
        line = self.readline()
        line = line.decode('utf-8')
        line = line.strip('\r\n')

        values = line.split('::')
        read_time = values[0].split('=')[1]
        temp = values[1].split('=')[1]

        return read_time, temp

    def set_read_frequency(freq):
        pass
