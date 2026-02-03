class PressureSensor:
    def __init__(self, _pressure: float):
        self.__pressure = _pressure
    def set_value(self, value: float):
        self.__pressure = value
        if 0.0 > value or value > 10.0:
            raise ValueError
    def update_reading(self):
        return self.__pressure
    signal = property(update_reading, set_value)

sensor_log = [2.5, 11.8, 11.0]
status_log = [{}]

sensor = PressureSensor(5)

for index, value in enumerate(sensor_log):
    try: 
        sensor.signal = value
        status_log.append({
            "id":index,
            "val": value,
            "status": "success"
        })
    except ValueError as err:
        print("Error:", err)
        status_log.append({
            "id": index,
            "val":value,
            "status": "error"
        })

print(status_log)