import requests
import os
import dotenv
import utils


dotenv.load_dotenv()
APIKEY = os.getenv("OCT_API_KEY")
# PRODUCT2 =
MPAN = os.getenv("MPAN")
METER_SERIAL = os.getenv("SERIAL")


def daily(to_date):
    print("Input date:", to_date)

    PERIOD_TO = "2023-10-02T01:29Z"
    PERIOD_FROM = "2020-10-01T00:00Z"
    PAGE_SIZE = 100

    URL = f"https://api.octopus.energy/v1/electricity-meter-points/{MPAN}/meters/{METER_SERIAL}/consumption/?page_size={PAGE_SIZE}&period_from={PERIOD_FROM}&period_to={PERIOD_TO}&order_by=period"
    r = requests.get(URL, auth=(APIKEY, ""))
    output_dict = r.json()
    return utils.extract_time(output_dict["results"])


# MAIN
if __name__ == '__main__':
    print("output_dict=")
    print(daily(1))
