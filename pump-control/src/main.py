from services import ENV, LOGGER
from services.bhyve import Bhyve
import time
import requests



'''
Main module
Simply check if a bhyve zone is active
Turn pump on with an off timer for failsafe
'''



def main():
    bhyve = Bhyve(ENV.ORBIT_USERNAME, ENV.ORBIT_PASSWORD)
    previous_zone_active = False
    while True:
        bhyve.get_devices()
        zone_active = bhyve.zone_active()
        if zone_active:
            requests.get(f"http://{ENV.SHELLY_PRO_1PM_HOST}/relay/0?turn=on&timer={ENV.SHELLY_PRO_1PM_FAILSAFE_SECONDS}")
        if zone_active != previous_zone_active:
            if zone_active:
                LOGGER.info("A Bhyve zone is now active, requested the pump relay to turn on...")
            else:
                LOGGER.info("No Bhyve zones are currently active, pump relay will turn off.")
            previous_zone_active = zone_active
            
        time.sleep(ENV.POLLING_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()