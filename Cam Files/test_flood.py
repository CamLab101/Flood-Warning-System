"""Unit test for the flood module"""

import pytest
from floodsystem.station import MonitoringStation
from floodsystem.flood import *

# Create stations
a = MonitoringStation("test-s-id1","test-m-id2","some station1",\
(-2.0, 4.0),(-2.3, 3.4445),"River 1","Town 1")
a.latest_level=3.4445

b = MonitoringStation("test-s-id1","test-m-id2","some station1",\
(-2.0, 4.0),(5, 9),"River 1","Town 1")
b.latest_level=11

c = MonitoringStation("test-s-id1","test-m-id2","some station1",\
(-2.0, 4.0),(2,12),"River 1","Town 1")
c.latest_level=10

d = MonitoringStation("test-s-id1","test-m-id2","some station1",\
(-2.0, 4.0),(2, 12),"River 1","Town 1")
d.latest_level=11

e = MonitoringStation("test-s-id1","test-m-id2","some station1",\
(-2.0, 4.0),(6, 0),"River 1","Town 1")
e.latest_level=2

test_stations = [a,b,c,d,e]

def test_stations_level_over_threshold():

    test_res = stations_level_over_threshold(test_stations,0.8)

    assert test_res == [(b,1.5),(a,1),(d,0.9)]

def test_stations_highest_rel_level():

    test_res = stations_highest_rel_level(test_stations,3)

    assert test_res == [b,a,d]
