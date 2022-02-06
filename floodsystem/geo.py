# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from ssl import SSL_ERROR_WANT_X509_LOOKUP
from floodsystem.station import MonitoringStation
from .utils import sorted_by_key  # noqa

#from haversine import haversine

'''
def stations_by_distance(stations,p):
    p=(52.053,0.1218)
    distance=(0,0)
    for station in stations:
        distance = haversine(p,stations.coord)
    x=sorted_by_key([(stations.name),(stations.town),(distance)],2)
    
    return x

'''


def rivers_with_station(stations):
    rivers = set() 
    for station in stations:
        rivers.add(station.river)
    return rivers 

def stations_by_river(stations):
    dictionary = {}
    for river in rivers_with_station(stations):
        listOfStations = []
        for station in stations:
            if station.river == river:
                listOfStations.append(station.name)    
        dictionary[river] = listOfStations      
    return dictionary 

def rivers_by_station_number(stations, N):
    listOfTuples = []
    for river in stations_by_river(stations).keys():
        numberTuple = (river,len(stations_by_river(stations)[river]))
        listOfTuples.append(numberTuple)
    listOfTuples.sort(key=lambda y: y[1], reverse = True)
    nth_value = listOfTuples[N - 1][1]    
    rivers_output = []
    for river in listOfTuples:
        if river[1] < nth_value:
            break
        rivers_output.append(river)
    return rivers_output



