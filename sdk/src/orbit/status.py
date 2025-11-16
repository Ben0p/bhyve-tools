from .wateringstatus import WateringStatus



'''
Orbit B-Hyve device status class
Child of the device class
'''



class Status():
    def __init__(self, data: dict):
        self._data: dict = data
    
    
    def __str__(self) ->str:
        return str(self.as_dict())
        

    def as_dict(self) -> dict:
        return {
            'run_mode' : self.run_mode,
            'next_start_programs' : self.next_start_programs,
            'rain_delay_overridden_at' : self.rain_delay_overridden_at,
            'watering_status' : self.watering_status.as_dict(),
            'status_updated_at' : self.status_updated_at,
            'next_start_time' : self.next_start_time,
            'watering-status' : self.wateringstatus
        }

        
    @property
    def run_mode(self) -> str | None:
        return self._data.get('run_mode')


    @property
    def next_start_programs(self) -> list[str] | None:
        return self._data.get('next_start_programs')


    @property
    def rain_delay_overridden_at(self) -> str | None:
        return self._data.get('rain_delay_overridden_at')


    @property
    def watering_status(self) -> WateringStatus | None:
        return WateringStatus(self._data.get('watering_status'))


    @property
    def status_updated_at(self) -> str | None:
        return self._data.get('status_updated_at')


    @property
    def next_start_time(self) -> str | None:
        return self._data.get('next_start_time')

        
    @property
    def wateringstatus(self) -> str | None:
        return self._data.get('watering-status')