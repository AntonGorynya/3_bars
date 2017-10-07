#! /usr/bin/python3

import json
import argparse


def load_data(filepath):
    with open(filepath, encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data


def get_biggest_bar(json_data):
    biggest_name_candidate = ''
    biggest_seats_candidate = 0
    biggest_seats = 0
    biggest_name = ['']
    for bar in json_data['features']:
        biggest_name_candidate = (bar['properties']['Attributes']['Name'])
        biggest_seats_candidate = (bar['properties']['Attributes']
                                   ['SeatsCount'])
        if biggest_seats_candidate > biggest_seats:
            biggest_seats = biggest_seats_candidate
            biggest_name = [biggest_name_candidate]
        elif biggest_seats_candidate == biggest_seats:
            biggest_name.append(biggest_name_candidate)
    if len(biggest_name) == 1:
        print('biggest bar is', biggest_name[0])
        print('biggest seats counts is ', biggest_seats)
    else:
        print('biggests bar are ')
        for bar in biggest_name:
            print('- ', bar)
        print('biggest seats counts is ', biggest_seats, end='\n\n')


def get_smallest_bar(json_data):
    smallest_name_candidate = (json_data['features'][0]
                               ['properties']['Attributes']['Name'])
    smallest_seats_candidate = (json_data['features'][0]
                                ['properties']['Attributes']['SeatsCount'])
    smallest_seats = (json_data['features'][0]
                      ['properties']['Attributes']['SeatsCount'])
    smallest_name = [json_data['features'][0]['properties']['Attributes']['Name']]
    for bar in json_data['features']:
        smallest_name_candidate = (bar['properties']['Attributes']['Name'])
        smallest_seats_candidate = (bar['properties']
                                    ['Attributes']['SeatsCount'])
        if smallest_seats_candidate < smallest_seats:
            smallest_seats = smallest_seats_candidate
            smallest_name = [smallest_name_candidate]
        elif smallest_seats_candidate == smallest_seats:
            smallest_name.append(smallest_name_candidate)
    if len(smallest_name) == 1:
        print('smallest bar is', smallest_name[0])
        print('smallest seats counts is ', smallest_seats)
    else:
        print('smallest bar are ')
        for bar in smallest_name:
            print('- ', bar)
        print('smallest seats counts is ', smallest_seats, end='\n\n')


def get_closest_bar(json_data, longitude, latitude):
    [bar_longitude, bar_latitude] = (json_data['features'][0]
                                     ['geometry']['coordinates'])
    closset_bar_name = [json_data['features'][0]['properties']['Attributes']['Name']]
    for bar in json_data['features']:
        closest_name_candidate = bar['properties']['Attributes']['Name']
        coordinate_candidate = bar['geometry']['coordinates']
        if ((coordinate_candidate[0]-longitude)**2+(coordinate_candidate[1]-latitude)**2) < ((bar_longitude-longitude)**2+(bar_latitude-latitude)**2):
            closset_bar_name = [closest_name_candidate]
            [bar_longitude, bar_latitude] = coordinate_candidate
        elif ((coordinate_candidate[0]-longitude)**2+(coordinate_candidate[1]-latitude)**2) == ((bar_longitude-longitude)**2+(bar_latitude-latitude)**2):
            closset_bar_name.append(closest_name_candidate)
    if len(closset_bar_name) == 1:
        print('Closset bar is', closset_bar_name[0])
    else:
        print('Clossets bar are ')
        for bar in closset_bar_name:
            print('- ', bar)


def create_parser():
    parser = argparse.ArgumentParser(description='--> Bar analys <--')
    parser.add_argument("path", nargs=1, help="path to json file")
    parser.add_argument("-b", action="store_true", help="get biggest bar(s)")
    parser.add_argument("-s", action="store_true", help="get smalest bar(s)")
    parser.add_argument("-c", nargs=2, help="get closset bar(s). "
                                            "Plese input your coordinate")
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    json_data = load_data(namespace.path[0])
    if namespace.path:
        if namespace.b:
            get_biggest_bar(json_data)
        if namespace.s:
            get_smallest_bar(json_data)
        if namespace.c:
            get_closest_bar(json_data, float(namespace.c[0]), float(namespace.c[1]))
        pass
