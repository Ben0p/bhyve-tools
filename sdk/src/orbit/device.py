from .address import Address
from .timezone import Timezone
from .location import Location
from .status import Status



'''
Class for a Bhyve device
'''



class Device():
    def __init__(self, data: dict):
        self._data: dict = data
    
    
    def __str__(self) ->str:
        return str(self.as_dict())
        

    def as_dict(self) -> dict:
        return {
            'last_connected_at' : self.last_connected_at,
            'address' : self.address.as_dict(),
            'water_sense_mode' : self.water_sense_mode,
            'timezone' : self.timezone.as_dict(),
            'full_location' : self.full_location,
            'weather_forecast_location_id' : self.weather_forecast_location_id,
            'firmware_version' : self.firmware_version,
            'name' : self.name,
            'type' : self.type,
            'battery' : self.battery,
            'network_interface' : self.network_interface,
            'restricted_frequency' : self.restricted_frequency,
            'weather_delay_thresholds' : self.weather_delay_thresholds,
            'updated_at' : self.updated_at,
            'reference' : self.reference,
            'mac_address' : self.mac_address,
            'weather_station_id' : self.weather_station_id,
            'mesh_id' : self.mesh_id,
            'status' : self.status.as_dict(),
            'wifi_version' : self.wifi_version,
            'id' : self.id,
            'num_stations' : self.num_stations,
            'zones' : self.zones,
            'user_id' : self.user_id,
            'google_home_status' : self.google_home_status,
            'device_gateway_topic' : self.device_gateway_topic,
            'smart_watering_enabled' : self.smart_watering_enabled,
            'hardware_version' : self.hardware_version,
            'location' : self.location.as_dict(),
            'created_at' : self.created_at,
            'suggested_start_time' : self.suggested_start_time,
            'et_id' : self.et_id
        }

        
    @property
    def last_connected_at(self) -> str | None:
        return self._data.get('last_connected_at')


    @property
    def address(self) -> Address:
        return Address(self._data.get('address'))


    @property
    def water_sense_mode(self) -> str | None:
        return self._data.get('water_sense_mode')


    @property
    def timezone(self) -> Timezone:
        return Timezone(self._data.get('timezone'))


    @property
    def full_location(self) -> None:
        # TODO
        return None


    @property
    def weather_forecast_location_id(self) -> str | None:
        return self._data.get('weather_forecast_location_id')


    @property
    def firmware_version(self) -> str | None:
        return self._data.get('firmware_version')


    @property
    def name(self) -> str | None:
        return self._data.get('name')


    @property
    def type(self) -> str | None:
        return self._data.get('type')


    @property
    def battery(self) -> str | None:
        return self._data.get('battery')


    @property
    def network_interface(self) -> str | None:
        return self._data.get('network_interface')


    @property
    def battery(self) -> str | None:
        return self._data.get('battery')


    @property
    def restricted_frequency(self) -> None:
        # TODO
        return None


    @property
    def weather_delay_thresholds(self) -> None:
        # TODO
        return None


    @property
    def updated_at(self) -> str | None:
        return self._data.get('updated_at')


    @property
    def reference(self) -> str | None:
        return self._data.get('reference')


    @property
    def mac_address(self) -> str | None:
        return self._data.get('mac_address')


    @property
    def weather_station_id(self) -> str | None:
        return self._data.get('weather_station_id')


    @property
    def mesh_id(self) -> str | None:
        return self._data.get('mesh_id')


    @property
    def status(self) -> Status:
        return Status(self._data.get('status'))


    @property
    def wifi_version(self) -> int | None:
        return self._data.get('wifi_version')


    @property
    def id(self) -> str | None:
        return self._data.get('id')


    @property
    def num_stations(self) -> int | None:
        return self._data.get('num_stations')


    @property
    def zones(self) -> None:
        # TODO
        return None


    @property
    def user_id(self) -> str | None:
        return self._data.get('user_id')


    @property
    def mesh_id(self) -> str | None:
        return self._data.get('mesh_id')


    @property
    def google_home_status(self) -> str | None:
        return self._data.get('google_home_status')


    @property
    def device_gateway_topic(self) -> str | None:
        return self._data.get('device_gateway_topic')


    @property
    def smart_watering_enabled(self) -> bool | None:
        return self._data.get('smart_watering_enabled')


    @property
    def hardware_version(self) -> str | None:
        return self._data.get('hardware_version')


    @property
    def is_connected(self) -> bool | None:
        return self._data.get('is_connected')


    @property
    def location(self) -> Location | None:
        return Location(self._data.get('location'))


    @property
    def created_at(self) -> str | None:
        return self._data.get('created_at')


    @property
    def suggested_start_time(self) -> str | None:
        return self._data.get('suggested_start_time')


    @property
    def et_id(self) -> str | None:
        return self._data.get('et_id')