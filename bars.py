#! /usr/bin/python3

import json
import argparse


def get_key(input_dict,input_value):
	for k,v in input_dict.items():
		if v == input_value:
			return k

def load_data(filepath):
    with open(filepath, encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data


def get_biggest_bar(json_data):
    bar = max(json_data['features'], key=lambda x:x['properties']['Attributes']['SeatsCount'])
    seats_count = bar['properties']['Attributes']['SeatsCount']
    for bar in json_data['features']:
        if  bar['properties']['Attributes']['SeatsCount']==seats_count:
            print(bar['properties']['Attributes']['Name'],bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(json_data):
    bar = min(json_data['features'], key=lambda x: x['properties']['Attributes']['SeatsCount'])
    seats_count = bar['properties']['Attributes']['SeatsCount']
    for bar in json_data['features']:
        if bar['properties']['Attributes']['SeatsCount'] == seats_count:
            print(bar['properties']['Attributes']['Name'], bar['properties']['Attributes']['SeatsCount'])


def get_closest_bar(json_data, longitude, latitude):
    bar = min(json_data['features'], key=lambda x: (x['geometry']['coordinates'][0]-longitude)**2-(x['geometry']['coordinates'][1]-latitude)**2)
    seats_count = bar['properties']['Attributes']['SeatsCount']
    print(bar['properties']['Attributes']['Name'], seats_count)



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
