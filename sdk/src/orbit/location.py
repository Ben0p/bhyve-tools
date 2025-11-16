


class Location():
    def __init__(self, data: dict):
        self._data: dict = data
    
    
    def __str__(self) ->str:
        return str(self.as_dict())
        

    def as_dict(self) -> dict:
        return {
            'type' : self.type,
            'coordinates' : self.coordinates
        }

        
    @property
    def type(self) -> str | None:
        return self._data.get('type')


    @property
    def coordinates(self) -> list[float, float] | None:
        return self._data.get('coordinates')