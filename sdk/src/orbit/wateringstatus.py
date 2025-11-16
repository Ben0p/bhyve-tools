from .station import Station
from .waterevent import WaterEvent



'''
Device -> Status -> Watering Status class
'''



class WateringStatus():
    def __init__(self, data: dict):
        self._data: dict = data
    
    
    def __str__(self) ->str:
        return str(self.as_dict())
        

    def as_dict(self) -> dict:
        return {
            'stations' : [station.as_dict() if station else None for station in self.stations],
            'current_station' : self.current_station,
            'water_event_index' : self.water_event_index,
            'session_id' : self.session_id,
            'water_event_queue' : [queue.as_dict() if queue else None for queue in self.water_event_queue],
            'status' : self.status,
            'current_time_remaining_sec' : self.current_time_remaining_sec,
            'rain_sensor_hold' : self.rain_sensor_hold,
            'program' : self.program,
            'started_watering_station_at' : self.started_watering_station_at,
            'total_run_time_sec' : self.total_run_time_sec,
            'water_instance_id' : self.water_instance_id
        }

        
    @property
    def stations(self) -> list[Station] | list[None]:
        if self._data.get('stations'):
            return [
                Station(station)
                for station
                in self._data.get('stations')
            ]
        else:
            return [None]


    @property
    def current_station(self) -> list[str] | None:
        return self._data.get('current_station')


    @property
    def water_event_index(self) -> str | None:
        return self._data.get('water_event_index')


    @property
    def session_id(self) -> str | None:
        return self._data.get('session_id')


    @property
    def water_event_queue(self) -> list[WaterEvent] | None:
        if self._data.get('water_event_queue'):
            return [WaterEvent(event) for event in self._data.get('water_event_queue')]
        else:
            return [None]


    @property
    def status(self) -> str | None:
        return self._data.get('status')

        
    @property
    def current_time_remaining_sec(self) -> str | None:
        return self._data.get('current_time_remaining_sec')

        
    @property
    def rain_sensor_hold(self) -> str | None:
        return self._data.get('rain_sensor_hold')


    @property
    def program(self) -> str | None:
        return self._data.get('program')


    @property
    def started_watering_station_at(self) -> str | None:
        return self._data.get('started_watering_station_at')


    @property
    def total_run_time_sec(self) -> str | None:
        return self._data.get('total_run_time_sec')


    @property
    def water_instance_id(self) -> str | None:
        return self._data.get('water_instance_id')


