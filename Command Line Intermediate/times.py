import pandas as pd
from dateutil.parser import parse
from datetime import *
import read

hours = read.load_data()

def extract_hours(timestamp):
    convert = parse(timestamp)
    hour = convert.hour
    return hour

def extract_day(timestamp):
    convert = parse(timestamp)
    day = convert.weekday()
    return day

if __name__ == "__main__":
    hours["submission_hour"] = hours["submission_time"].apply(extract_hours)
    hours["submission_day"] = hours["submission_time"].apply(extract_day)
    print(hours["submission_hour"].value_counts())
    print(hours["submission_day"].value_counts())
    