# POTA Local Parks Progress Script
# By Ian Renton, November 2024
# Queries the Parks on the Air API to find your closest parks, and prints the status of whether
# you have activated them.
# See the README.md file for more details.
# This is Public Domain software, see the LICENCE file

from requests_cache import CachedSession
from datetime import timedelta
import great_circle_calculator.great_circle_calculator as gcc
import sys

# Parse command-line arguments
if len(sys.argv) != 5:
    print("The script must be run with exactly 4 command-line arguments. See README for details.")

num_parks = int(sys.argv[1])
callsign = sys.argv[2]
lat = float(sys.argv[3])
lon = float(sys.argv[4])

# Fetch list of parks within +-1 degree lat/lon of your location.
session = CachedSession("pota-local-progress-cache", expire_after=timedelta(days=1))
parks = session.get(
    "https://api.pota.app/park/grids/" + str(lat - 1.0) + "/" + str(lon - 1.0) + "/" + str(lat + 1.0) + "/" + str(
        lon + 1.0) + "/0").json()

# For each park, calculate its distance and store it with the rest of the data
parks = parks["features"]
print("Found " + str(len(parks)) + " parks")
home = (lon, lat)
for park in parks:
    park_loc = (park["geometry"]["coordinates"][0], park["geometry"]["coordinates"][1])
    park["properties"]["distance_from_home"] = gcc.distance_between_points(home, park_loc, unit='kilometers',
                                                                           haversine=True)

# Sort parks by distance from you, and limit to the number we are insterested in
parks.sort(key=lambda x: x["properties"]["distance_from_home"])
parks = parks[:num_parks]

# Write output
print("The closest " + str(num_parks) + " parks to " + callsign + " QTH at " + str(lat) + ", " + str(lon) + " are:")
print("  Status  | Distance | Reference | Name")
print("----------|----------|-----------|----------------------------------------------")
for park in parks:
    limited_len_name = (park["properties"]["name"][:43] + '..') if len(park["properties"]["name"]) > 43 else \
      park["properties"]["name"]
    print("Activated".center(9) + " | "
          + ("{:.1f}".format(park["properties"]["distance_from_home"]) + " km").rjust(8) + " | "
          + park["properties"]["reference"].center(9) + " | " + limited_len_name)
