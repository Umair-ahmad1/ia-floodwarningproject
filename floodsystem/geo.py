# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from floodsystem.station import MonitoringStation
from .utils import sorted_by_key  # noqa
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers.
    return c * r


def stations_by_distance(stations,p):
    distance=[]
    for station in stations:
        distance.append((station, haversine(p[0],p[1],station.coord[0],station.coord[1])))
    x=sorted_by_key(distance,1)
    
    return x

def stations_within_radius(stations,centre,r):
    distance=[]
    lengths=[]
    for station in stations:
        distance.append((station, haversine(centre[0],centre[1],station.coord[0],station.coord[1])))
    for x in range(len(distance)):
        if distance[1]<r:
            lengths.append((station, haversine(centre[0],centre[1],station.coord[0],station.coord[1])))
    lengths=sorted_by_key(lengths,0)

    return lengths 
