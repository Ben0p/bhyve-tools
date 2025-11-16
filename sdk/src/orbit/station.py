


class Station():
    def __init__(self, data: dict):
        self._data: dict = data
    
    
    def __str__(self) ->str:
        return str(self.as_dict())
        

    def as_dict(self) -> dict:
        return {
            'station' : self.station,
            'run_time' : self.run_time
        }

        
    @property
    def station(self) -> int | None:
        return self._data.get('station')


    @property
    def run_time(self) -> float | None:
        return self._data.get('run_time')