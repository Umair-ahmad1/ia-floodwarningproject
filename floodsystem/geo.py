# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.station import MonitoringStation
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations,p):
    p=(52.053,0.1218)
    #stations will be a list of data then take the relevant parts of the data for each part of the formula
    #then with p, use the haversine formula to give the distance away from cambridge
    #so create a new list taking the station name,town,and the calculate distance away from p above
    #sort this final list with the sorted_by_key function to sort by the distance
    #for task 1b

def stations_within_radius(stations,centre,r):
    r=10
    centre=(52.053,0.1218)
    #stations will contain the names and the geographic co-ordinate
    #station geographic co-ordinate used again with the haversine formula
    #if the haversine formula result is greater than the radius do not add to the list
    #then sort the results by alphabetic, so by the first part of the list
    #for 1c

    