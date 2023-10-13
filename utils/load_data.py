"""File containing functions for loading test data"""

from csv import reader
import json


def load_csv_data(path: str) -> list[tuple]:
    """Load csv data for test parametrization."""
    with open(path, "r") as f:
        # create csv reader object
        csv_reader = reader(f)

        # skip the header row
        next(csv_reader)

        # transform csv rows into a list of tuples
        return list(map(tuple, csv_reader))


def load_json_data(path: str) -> list[tuple]:
    """Load json data for test parametrization"""
    with open(path, "r") as f:
        # load the json data
        data = json.load(f)

        # transform json values into a list of tuples
        return [tuple(d.values()) for d in data]
