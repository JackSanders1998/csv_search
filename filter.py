import sys
import pandas as pd

"""
README
Custom filter helper

USAGE
python3 <this project> <path to directory of file to filter> <path to file containing filtered records>
python3 /Users/jack/filter.py /Users/jack/records.csv /Users/jack/filtered_records.csv
"""


def main(args):
    df = pd.read_csv(args[1])
    filtered_search = df[df["BorrowerState"] == "IL"]
    filtered_search.to_csv(args[2])
    print(filtered_search.count())


if __name__ == "__main__":
    main(sys.argv)
