import pandas as pd
import read

domains = read.load_data()

top_20_domains = domains["url"].value_counts()[:20]

if __name__ == "__main__":
    print(top_20_domains)