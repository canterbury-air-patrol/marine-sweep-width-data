#!/usr/bin/env python3

import os
import csv
import json

corrections_file = 'weather_correction_types.csv'
directory = 'source-data'

data = {}

def merge_sw_distance(sweep_widths, distances):
    result = []
    last_sw = -1
    for sw, viz in zip(sweep_widths, distances):
        if sw == last_sw:
            continue
        result.append({'sw': float(sw), 'vis': float(viz)})
        last_sw = sw
    return result

def load_corrections(corrections_file):
    with open(corrections_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if line[0] not in data:
                data[line[0]] = {}
            data[line[0]]['weather_corrections'] = line[1]


def load_sweep_widths(directory):
    for f in os.listdir(directory):
        short_name = f.split('.')[0]
        asset_type, height = short_name.split('-')

        filename = os.path.join(directory, f)
        if os.path.isfile(filename):
            distances = []
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for line in reader:
                    if line[0] == 'Search Object':
                        distances = line[1:]
                        continue
                    if line[0] not in data:
                        data[line[0]] = {}
                    if asset_type not in data[line[0]]:
                        data[line[0]][asset_type] = {}
                    data[line[0]][asset_type][height] = merge_sw_distance(line[1:],distances)

load_corrections(corrections_file)
load_sweep_widths(directory)

with open('marine-sweep-width-data-table.js', 'w') as output:
    output.write('const marine_sweep_widths =\n')
    output.write(json.JSONEncoder().encode(data))
    output.write(';\n')
    output.write('export { marine_sweep_widths };')