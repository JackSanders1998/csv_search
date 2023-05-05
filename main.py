import sys
import os
import pandas as pd

"""
README
Gets all CSVs in a directory and searches for all keywords across the files.
Tracks all hits and writes to a csv in the same directory passed in to save search results.

USAGE
python3 <this project> <path to directory of files to search> <keywords to search for; space seperated>
python3 /Users/jack/main.py /Users/jack/records 'Jack Sanders' 'November' '14' '1998'
"""


def main(args):
    # gather user input
    dir_list = os.listdir(args[1])
    # filter out hidden files
    dir_list = [file for file in dir_list if not file.startswith('.')]
    keyword_list_raw = args[2:]
    # format keywords to be passed into str.contains
    keywords = ""
    for key in keyword_list_raw:
        keywords += key.lower() + '|'
    keywords = keywords[:-1]

    print(f"searching for {len(keywords.split('|'))} keyword(s) across {len(dir_list)} files in the {args[1]} directory")

    # search result will be stored in this list
    frames = []

    # loop through files in the directory the user passed in
    for file in dir_list:
        # create the dataframe
        try:
            print(f"creating {args[1]}/{file} dataframe")
            df = pd.read_csv(f"{args[1]}/{file}", engine='python', encoding='utf-8', on_bad_lines='skip')
            cols = list(df.columns.values)

            print(f"searching {args[1]}/{file} with {len(cols)} columns")

            # loop through columns in the dataframe
            for col in cols:
                # search for keywords
                search = df[df[col].astype(str).str.lower().str.contains(keywords, na=False) & df["BorrowerState"] == "IL"]
                if not search.empty:
                    print(search)
                    frames.append(search)
        except UnicodeWarning:
            continue

    search_results = pd.concat(frames)
    search_results.to_csv(f"{args[1]}/search_results.csv")


if __name__ == "__main__":
    main(sys.argv)
