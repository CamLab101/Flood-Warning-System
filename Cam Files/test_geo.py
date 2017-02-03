"""Unit test for the geo module"""
import pytest
#build list of test stations
from floodsystem.station import MonitoringStation
test1=MonitoringStation('s_id1','m_id1','name1',(51,-1), (0.15, 0.895), 'river1', 'town1')
test2=MonitoringStation('s_id2','m_id2','name2',(52,-0.1), (0.5, 0.42), 'river2', 'town2')
test3=MonitoringStation('s_id3','m_id3','name3',(0,0), None , 'river3', 'town3')
test_list=[test1,test2,test3]

#for task 1D
from floodsystem.geo import rivers_with_station
def test_rivers_with_station():
	assert rivers_with_station(test_list) == ['river1','river2','river3']

from floodsystem.geo import stations_by_river
def test_station_by_river():
	assert stations_by_river(test_list)['river1']==['name1']
	assert stations_by_river(test_list)['river2']==['name2']

#for task 1E
from floodsystem.geo import rivers_by_station_number
def test_rivers_by_station_number():
	assert rivers_by_station_number(test_list,1)[0]==('river2', 1)

#for 1F
from floodsystem.station import inconsistent_typical_range_stations
def test_inconsistent_typical_range_stations():
	assert inconsistent_typical_range_stations(test_list) ==['name2','name3']