


class WaterEvent():
    def __init__(self, data: dict):
        self._data: dict = data
    
    
    def __str__(self) ->str:
        return str(self.as_dict())
        

    def as_dict(self) -> dict:
        return {
            'station' : self.station,
            'run_time_sec' : self.run_time_sec
        }

        
    @property
    def station(self) -> int | None:
        return self._data.get('station')


    @property
    def run_time_sec(self) -> int | None:
        return self._data.get('run_time_sec')