import pandas as pd
import read
from collections import Counter

data_count = read.load_data()

headlines_str = " "

for i in data_count["headline"]:
    add_space = str(i) + " "
    headlines_str += str(add_space)
    
headlines_str = headlines_str.lower()

words = headlines_str.split()

top_100 = Counter(words).most_common(100)


if __name__ == "__main__":
    print(top_100)