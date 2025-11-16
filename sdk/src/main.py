from services import ENV, LOGGER
from orbit import Bhyve
import time



def main():
    bhyve = Bhyve(ENV.ORBIT_USERNAME, ENV.ORBIT_PASSWORD)
    while True:
        LOGGER.info(bhyve.zone_active)
        time.sleep(ENV.POLLING_INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
