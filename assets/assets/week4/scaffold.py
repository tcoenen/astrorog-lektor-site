#!/usr/env/bin python


def read_station_locations(file_obj):

    # look for start of the first part of the header
    for line in file_obj:
        if line.startswith('# STN'):
            break

    # parse the station locations until an empty line is reached
    station_locations = []
    for line in file_obj:
        if line.startswith('#') and not line[1:].strip():
            break

        # parsing code goes here:
        print 'STATION LOCATION', line

    return station_locations


def read_abbreviations(file_obj):
    # parse abbreviations until an empty line is reached
    abbreviations = {}
    for line in file_obj:
        if line.startswith('#') and not line[1:].strip():
            break

        # parsing code goes here
        print 'ABBREVIATOIN', line

    return abbreviations


def read_column_names(file_obj):
    """Read column names from KNMI data file"""
    column_names = [cn.strip() for cn in next(file_obj).split(',')[1:]]

    return column_names


def read_data(file_obj):
    """Read the weather observations from the KNMI data file"""
    pass  # parse the body of the data file here


def read_knmi_data_file(filename):
    """Fully parse the KNMI data file"""
    with open(filename, 'r') as f:
        station_locations = read_station_locations(f)
        abbreviations = read_abbreviations(f)
        column_names = read_column_names(f)

        data = read_data(f)

    return station_locations, abbreviations, column_names, data


def plot_max_temperature(data, station_number):
    """Given its number plot max temperature over time at a weather station"""
    pass


def main():
    """Parse the KNMI data file and plot the max temperature at the Bilt."""
    station_locations, abbreviations, column_names, data = \
        read_knmi_data_file('chunk.txt')
    plot_max_temperature(data, station_number=260)


if __name__ == '__main__':
    main()
