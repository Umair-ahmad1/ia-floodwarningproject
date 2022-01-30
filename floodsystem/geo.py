# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.station import MonitoringStation
from .utils import sorted_by_key  # noqa
pip install haversine
from haversine import haversine, km


def stations_by_distance(stations,p):
    p=(52.053,0.1218)
    distance=(0,0)
    for station in stations:
        distance = haversine(p,stations.coord)
    x=sorted_by_key([(stations.name),(stations.town),(distance)]2)
    
    print(x)
return
def stations_within_radius(stations,centre,r):
    r=10
    centre=(52.053,0.1218)
    #stations will contain the names and the geographic co-ordinate
    #station geographic co-ordinate used again with the haversine formula
    #if the haversine formula result is greater than the radius do not add to the list
    #then sort the results by alphabetic, so by the first part of the list
    #for 1c
return

    