


class Timezone():
    def __init__(self, data: dict):
        self._data: dict = data
    
    
    def __str__(self) ->str:
        return str(self.as_dict())
        

    def as_dict(self) -> dict:
        return {
            'dst_offset' : self.dst_offset,
            'raw_offset' : self.raw_offset,
            'timezone_id' : self.timezone_id,
            'timezone_name' : self.timezone_name
        }

        
    @property
    def dst_offset(self) -> int | None:
        return self._data.get('dst_offset')


    @property
    def raw_offset(self) -> int | None:
        return self._data.get('raw_offset')


    @property
    def timezone_id(self) -> str | None:
        return self._data.get('timezone_id')


    @property
    def timezone_name(self) -> str | None:
        return self._data.get('timezone_name')