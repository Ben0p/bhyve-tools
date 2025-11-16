


class Address():
    def __init__(self, data: dict):
        self._data: dict = data
    
    
    def __str__(self) ->str:
        return str(self.as_dict())
        

    def as_dict(self) -> dict:
        return {
            'line_1' : self.line_1,
            'city' : self.city,
            'state' : self.state,
            'postal_code' : self.postal_code,
            'country' : self.country
        }

        
    @property
    def line_1(self) -> str | None:
        return self._data.get('line_1')


    @property
    def city(self) -> str | None:
        return self._data.get('city')


    @property
    def state(self) -> str | None:
        return self._data.get('state')


    @property
    def postal_code(self) -> str | None:
        return self._data.get('postal_code')


    @property
    def country(self) -> str | None:
        return self._data.get('country')