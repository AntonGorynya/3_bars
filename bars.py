#! /usr/bin/python3

import json
import argparse


def get_key(input_dict, input_value):
    for dict_key, dict_value in input_dict.items():
        if dict_value == input_value:
            return dict_key


def load_data(filepath):
    with open(filepath, encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data


def get_biggest_bar(json_data):
    print("самые большие бары:")
    bar = max(json_data['features'],
              key=lambda x: x['properties']['Attributes']['SeatsCount'])
    seats_count = bar['properties']['Attributes']['SeatsCount']
    for bar in json_data['features']:
        bar_attributes = bar['properties']['Attributes']
        if bar_attributes['SeatsCount'] == seats_count:
            print("  -", bar['properties']['Attributes']['Name'],
                  bar_attributes['SeatsCount'], "сидячих мест")


def get_smallest_bar(json_data):
    print("самые маленькие бары:")
    bar = min(json_data['features'],
              key=lambda x: x['properties']['Attributes']['SeatsCount'])
    seats_count = bar['properties']['Attributes']['SeatsCount']
    for bar in json_data['features']:
        bar_attributes = bar['properties']['Attributes']
        if bar_attributes['SeatsCount'] == seats_count:
            print("  -", bar['properties']['Attributes']['Name'],
                  bar_attributes['SeatsCount'], "сидячих мест")


def get_closest_bar(json_data, longitude, latitude):
    print("ближайший бар:")
    bar = min(json_data['features'],
              key=lambda x: (x['geometry']['coordinates'][0]-longitude)**2 -
                            (x['geometry']['coordinates'][1]-latitude)**2)
    seats_count = bar['properties']['Attributes']['SeatsCount']
    print(bar['properties']['Attributes']['Name'], seats_count, "сидячих мест")


def create_parser():
    parser = argparse.ArgumentParser(description='--> Bar analys <--')
    parser.add_argument("path", help="path to json file")
    parser.add_argument("-b", action="store_true", help="get biggest bar(s)")
    parser.add_argument("-s", action="store_true", help="get smalest bar(s)")
    parser.add_argument("-c", nargs=2, help="get closset bar(s). "
                                            "Plese input your coordinate")
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    json_data = load_data(args.path)
    if args.path:
        if args.b:
            get_biggest_bar(json_data)
        if args.s:
            get_smallest_bar(json_data)
        if args.c:
            get_closest_bar(json_data, float(args.c[0]),
                            float(args.c[1]))
