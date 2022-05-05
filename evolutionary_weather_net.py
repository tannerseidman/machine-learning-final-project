#!/usr/bin/python3

import csv, math

from datetime import datetime as dt

def is_valid_number(str_num):
    for char in str_num:
        if not char.isnumeric() or not char == '-' or not char = '.':
            return False
    return True

def load_data(input_files):
    loaded_data = []
    for filename in input_files:
        with open(filename) as data:
            reader = csv.DictReader(data)
            for row in reader:
                date = dt.fromisoformat(row['DATE'])
                dry_bulb = 0.0
                wet_bulb = 0.0
                pressure = 0.0

                str_dry_bulb = row['HourlyDryBulbTemperature']
                str_wet_bulb = row['HourlyWetBulbTemperature']
                str_pressure = row['HourlyStationPressure']

                if is_valid_number(str_dry_bulb): dry_bulb = float(str_dry_bulb)
                if is_valid_number(str_wet_bulb): wet_bulb = float(str_wet_bulb)
                if is_valid_number(str_pressure): pressure = float(str_pressure)

                loaded_data.append({ 'date': date,
                                 'dry_bulb': dry_bulb,
                                 'wet_bulb': wet_bulb,
                                 'pressure': pressure })
    return loaded_data

# Blacksburg data
bb_train_1 = load_data(["blacksburg/2010.csv", "blacksburg/2011.csv", "blacksburg/2012.csv"])
bb_validation_1 = load_data(["blacksburg/2013.csv"])
bb_train_2 = load_data(["blacksburg/2014.csv", "blacksburg/2015.csv", "blacksburg/2016.csv"])
bb_validation_2 = load_data(["blacksburg/2017.csv"])
bb_train_3 = load_data(["blacksburg/2018.csv", "blacksburg/2019.csv", "blacksburg/2020.csv"])
bb_validation_3 = load_data(["blacksburg/2021.csv"])
bb_train = [bb_train_1, bb_train_2, bb_train_3]
bb_valid = [bb_validation_1, bb_validation_2, bb_validation_3]

# San Francisco data
sf_train_1 = load_data(["sanfrancisco/2010.csv", "sanfrancisco/2011.csv", "sanfrancisco/2012.csv"])
sf_validation_1 = load_data(["sanfrancisco/2013.csv"])
sf_train_2 = load_data(["sanfrancisco/2014.csv", "sanfrancisco/2015.csv", "sanfrancisco/2016.csv"])
sf_validation_2 = load_data(["sanfrancisco/2017.csv"])
sf_train_3 = load_data(["sanfrancisco/2018.csv", "sanfrancisco/2019.csv", "sanfrancisco/2020.csv"])
sf_validation_3 = load_data(["sanfrancisco/2021.csv"])
sf_train = [sf_train_1, sf_train_2, sf_train_3]
sf_valid = [sf_validation_1, sf_validation_2, sf_validation_3]

# Dublin data
db_train_1 = load_data(["dublin/2010.csv", "dublin/2011.csv", "dublin/2012.csv"])
db_validation_1 = load_data(["dublin/2013.csv"])
db_train_2 = load_data(["dublin/2014.csv", "dublin/2015.csv", "dublin/2016.csv"])
db_validation_2 = load_data(["dublin/2017.csv"])
db_train_3 = load_data(["dublin/2018.csv", "dublin/2019.csv", "dublin/2020.csv"])
db_validation_3 = load_data(["dublin/2021.csv"])
db_train = [db_train_1, db_train_2, db_train_3]
db_valid = [db_validation_1, db_validation_2, db_validation_3]

def identity_fn(x):
    return x

def threshold_fn(x):
    if x >= 0:
        return 1
    else:
        return -1

def sigmoid_fn(x):
    return 1/(1+exp(-x))

def gaussian_fn(x):
    u = None # need to figure out u
    sigma = None # need to figure out sigma; avg?
    power = -1/2 * ((x-u)/sigma)^2

def tanh_fn(x):
    return (exp(x) - exp(-x))/(exp(x) + exp(-x))

class Node:
    def __init__(self, input_nodes, weights, output_nodes, activation_fn):
        self.input_nodes = input_nodes
        self.weights = weights
        self.output_nodes = output_nodes
        self.activation_fn = activation_fn

        # Output sent to output_nodes
        self.output = None

    def update(self):
        inputs = [node.output for node in input_nodes]
    
        weighted_sum = sum([x*w for x, w in zip(inputs, weights)])
        weighted_sum += 1           # for bias
    
        self.output = self.activation_fn(weighted_sum)

class InputNode:
    def __init__(self, input):
        self.output = input

    def update(self):
        None

    def input(self, input):
        self.output = input
