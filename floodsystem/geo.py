# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from floodsystem.station import MonitoringStation
from .utils import sorted_by_key  # noqa

from haversine import haversine


def stations_by_distance(stations,p):
    p=(52.053,0.1218)
    distance=(0,0)
    for station in stations:
        distance = haversine(p,stations.coord)
    x=sorted_by_key([(stations.name),(stations.town),(distance)],2)
    
    return x

def stations_by_radius(stations,centre,p):
    for station in stations:
        if distance <10:
            #add to list 


    