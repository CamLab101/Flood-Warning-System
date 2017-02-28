import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    #build a list of station names with highest level
    list_of_names=[]
    list_of_tuples=stations_highest_rel_level(stations,5)
    for station in list_of_tuples:
      list_of_names.append (station[0])

    #find station, building list of require stations
    station_data=[]
    for name in list_of_names:
        for station in stations:
            if station.name == name:
                station_data.append (station)

    #Plot graph seperatedly regarding to each station
    for station in station_data:
        dt = 3
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        #make lists of date and lavel
        plot_water_level_with_fit(station.name, dates, levels, 4)
run()