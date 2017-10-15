#! /usr/bin/python3

import json
import argparse


def load_data(filepath):
    with open(filepath, encoding='utf-8') as input_file:
        json_data = json.load(input_file)
    return json_data


def get_biggest_bar(json_data):
    bars = json_data['features']
    biggest_bars = []
    bar = max(bars,
              key=lambda x: x['properties']['Attributes']['SeatsCount'])
    seats_count = bar['properties']['Attributes']['SeatsCount']
    for bar in bars:
        bar_attributes = bar['properties']['Attributes']
        if bar_attributes['SeatsCount'] == seats_count:
            biggest_bars.append(bar_attributes)
    return biggest_bars


def get_smallest_bar(json_data):
    bars = json_data['features']
    smallest_bars = []
    bar = min(bars,
              key=lambda x: x['properties']['Attributes']['SeatsCount'])
    seats_count = bar['properties']['Attributes']['SeatsCount']
    for bar in bars:
        bar_attributes = bar['properties']['Attributes']
        if bar_attributes['SeatsCount'] == seats_count:
            smallest_bars.append(bar_attributes)
    return smallest_bars


def get_closest_bar(json_data, longitude, latitude):
    bars = json_data['features']
    bar = min(bars,
              key=lambda x: (x['geometry']['coordinates'][0]-longitude)**2 +
                            (x['geometry']['coordinates'][1]-latitude)**2)
    return bar['properties']['Attributes']


def create_parser():
    parser = argparse.ArgumentParser(description='--> Bar analys <--')
    parser.add_argument("path", help="path to json file")
    parser.add_argument("-b", action="store_true", help="get biggest bar(s)")
    parser.add_argument("-s", action="store_true", help="get smalest bar(s)")
    parser.add_argument("-c", nargs=2, help="get closset bar(s). "
                                            "Plese input your coordinate")
    return parser


def print_bar(json_data, args):
    if args.b:
        print("\nCамые большие бары:")
        for bar in get_biggest_bar(json_data):
            print("{} количесво сидячих мест: {}"
                  .format(bar['Name'], bar['SeatsCount']))
    if args.s:
        print("\nCамые маленькие бары:")
        for bar in get_smallest_bar(json_data):
            print("{} количесво сидячих мест: {}"
                  .format(bar['Name'], bar['SeatsCount']))
    if args.c:
        print("\nближайший бар:")
        bar = get_closest_bar(json_data, float(args.c[0]), float(args.c[1]))
        print("{} количесво сидячих мест: {}"
              .format(bar['Name'], bar['SeatsCount']))


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    json_data = load_data(args.path)
    if args.path:
        print_bar(json_data, args)
