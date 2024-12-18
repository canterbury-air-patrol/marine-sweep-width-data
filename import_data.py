#!/usr/bin/env python3

import os
import csv
import json

corrections_file = 'weather_correction_types.csv'
directory = 'source-data'
speed_correction_files = ('Aircraft_speed_modifier.csv', 'Helicopter_speed_modifier.csv')

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

def merge_speed_correction(corrections, speeds):
    result = []
    last_correction = -1
    for correction, speed in zip(corrections, speeds):
        if correction == last_correction:
            continue
        result.append({'speed': int(speed), 'correction': float(correction)})
        last_correction = correction
    return result

def load_corrections(corrections_file):
    with open(corrections_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if line[0] not in data:
                data[line[0]] = {}
            data[line[0]]['weather_corrections'] = line[1]

def load_speed_corrections(corrections_file):
    asset_type = corrections_file.split('_')[0]
    with open(corrections_file, 'r') as csvfile:
        speeds = []
        reader = csv.reader(csvfile)
        for line in reader:
            if line[0] == 'Search Object':
                speeds = line[1:]
                continue
            if line[0] not in data:
                data[line[0]] = {}
            if 'speed_corrections' not in data[line[0]]:
                data[line[0]]['speed_corrections'] = {}
            data[line[0]]['speed_corrections'][asset_type] = merge_speed_correction(line[1:],speeds)

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
for correction_file in speed_correction_files:
    load_speed_corrections(correction_file)
load_sweep_widths(directory)

with open('marine-sweep-width-data-table.ts', 'w') as output:
    output.write('import { MarineSweepWidthData } from "./marine-sweep-width-types";\n')
    output.write('const marine_sweep_widths: MarineSweepWidthData =\n')
    output.write(json.JSONEncoder().encode(data))
    output.write(';\n')
    output.write('export { marine_sweep_widths };')