"""File containing functions for loading test data"""

from csv import reader


def load_csv_data(path: str) -> list[tuple]:
    """Load csv data for test parametrization."""
    with open(path, "r") as f:
        # create csv reader object
        csv_reader = reader(f)

        # skip the header row
        next(csv_reader)

        # transform csv rows into a list of tuples
        return list(map(tuple, csv_reader))
