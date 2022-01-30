#print the second function from geo stations_within_radius, giving a value for r as 10
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
stations = build_station_list()
centre=(52.2053,0.1218)
r=10.0
radial_distances = stations_within_radius(stations,centre,r)
print(radial_distances)