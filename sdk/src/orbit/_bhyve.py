from .bhyvesession import BhyveSession
from requests import Session
from . import const
from .device import Device
import time





class Bhyve():
    def __init__(self, username: str, password: str):
        self._username: str = username
        self._password: str = password
        self._session: Session = None
        self._bhyve_session: BhyveSession = None
        self._devices: list[dict] = None
        self._init_session()
        self._authenticate()
        self._get_devices()
    
    
    def _init_session(self) -> None:
        self._session = Session()
        self._session.headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json; charset=utf-8;",
            "User-Agent" : (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/72.0.3626.81 Safari/537.36"
            )      
        }
        
    
    def _authenticate(self) -> None:
        url: str = f"{const.API_HOST}{const.LOGIN_PATH}"
        json = {"session": {"email": self._username, "password": self._password}}

        response = self._session.request(
            method="post",
            url=url,
            json=json
        )
        response_json = response.json()
        self._bhyve_session = BhyveSession(response_json)
        
        self._session.headers["Orbit-Session-Token"] = self._bhyve_session.orbit_session_token

   
    def _get_devices(self) -> None:
        url = f"{const.API_HOST}{const.DEVICES_PATH}"
        params={"t": str(time.time())}
        response = self._session.get(
            url=url,
            params=params
        )
        self._devices = response.json()


    @property
    def bhyve_session(self) -> BhyveSession:
        return self._bhyve_session
    
    
    @property
    def devices(self) -> list[Device]:
        self._get_devices()
        return [Device(device) for device in self._devices]

   
    @property
    def zone_active(self) -> bool:
        
        for device in self.devices:
           if device.status.watering_status.status:
               return True
        return False