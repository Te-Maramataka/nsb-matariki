import json
import urllib.request
import time


url = r'https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND=%27301%27&OBJ_DATA=%27YES%27&MAKE_EPHEM=%27YES%27&EPHEM_TYPE=%27OBSERVER%27&CENTER=%27500@399%27&START_TIME=%272022-06-19%27&STOP_TIME=%272022-07-30%27&STEP_SIZE=%271%20d%27&QUANTITIES=%2724'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)
