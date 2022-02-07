from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key


stations=build_station_list()
inconsistent_data= inconsistent_typical_range_stations(stations)
y= sorted_by_key(inconsistent_data,0)
print(y)
