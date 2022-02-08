from floodsystem.geo import *
from floodsystem.stationdata import build_station_list


def test_stations_by_distance():
    
    stations = build_station_list()
    p = (51.47, -0.609)
    sorted_stations = stations_by_distance(stations, p)
    assert len(stations) == len(sorted_stations)
    for x in range(len(stations) - 1):
       assert sorted_stations[x][1] <= sorted_stations[x + 1][1]
    

def test_stations_within_radius():
    
    stations = build_station_list()
    p = (51.47, -0.609)
    stations_in = stations_within_radius(stations, p, 10)
    assert len(stations_in) == 27


def test_rivers_with_station():

    stations = build_station_list()

    rivers  = rivers_with_station(stations)

    assert len(rivers) != 0


def test_stations_by_river():

    stations = build_station_list()
    rivers_and_stations = stations_by_river(stations)
    assert len(rivers_and_stations) == len(rivers_with_station(stations))

    total = 0
    for value in rivers_and_stations.values():
        assert len(value)
        total += len(value)
    assert total == len(stations)

def test_rivers_by_station_number():

    stations = build_station_list()
    n = 9
    rivers_station_number = rivers_by_station_number(stations, n)
    
    #Test function output
    N = 0
    x = 0
    for river in rivers_station_number:
        if x != 0:
            if river[1] < rivers_station_number[x-1][1]:
                x += 1
                N += 1
            elif river[1] == rivers_station_number[x-1][1]:
                x += 1
        elif x == 0:
            x += 1
            N += 1
    assert N == n