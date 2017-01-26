from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station

stations=build_station_list()
#def run():
#    dict =rivers_with_station(stations)
#    rivers=[]
#    for river in dict:
#        rivers.append(river)
#    rivers.sort()
#    return print (rivers[:10])
#run()
rivers=rivers_with_station(stations)
rivers.sort()
print(rivers[:10])