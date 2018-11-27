import pandas as pd

def load_data():
    data = pd.read_csv("hn_stories.csv",header=None, names=["submission_time", "upvotes", "url", "headline"])
    return data

if __name__ == "__main__":
    hn_data = load_data()
    print(hn_data.head())