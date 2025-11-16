from requests import Session
import time
from pprint import pprint


'''
Basic Orbit Bhyve class
'''



class Bhyve():
    API_HOST = "https://api.orbitbhyve.com"
    LOGIN_PATH = "/v1/session"
    DEVICES_PATH = "/v1/devices"
    

    def __init__(self, username: str, password: str) -> None:
        self._username: str = username
        self._password: str = password
        self._session: Session = None
        self.devices: list[dict] = []
        self._init_session()
        self.authenticate()


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
        

    def authenticate(self) -> str:
        url: str = f"{self.API_HOST}{self.LOGIN_PATH}"
        json = {"session": {"email": self._username, "password": self._password}}

        response = self._session.request(
            method="post",
            url=url,
            json=json
        )
        response_json = response.json()
        self._session.headers["Orbit-Session-Token"] = response_json['orbit_session_token']


    def get_devices(self) -> None:
        url = f"{self.API_HOST}{self.DEVICES_PATH}"
        params={"t": str(time.time())}
        response = self._session.get(
            url=url,
            params=params
        )
        self.devices = response.json()
        
    
    def zone_active(self) -> bool:
        return any(
            device.get('status', {})
                .get('watering_status', {})
                .get('status') == 'watering_in_progress'
            for device in self.devices
        )