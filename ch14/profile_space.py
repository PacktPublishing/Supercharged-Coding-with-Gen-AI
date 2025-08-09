import pandas as pd
from memory_profiler import profile


@profile
def get_top_video(path):
    interactions = pd.read_csv(path)
    avg_ratio = interactions.mean(axis=0, skipna=True)
    return avg_ratio.idxmax()


print("top video: ", get_top_video('interactions_100.csv'))

# Profiling memory consumption across multiple runs
paths = [
    'interactions_100.csv',
    #    'interactions_1000.csv',
    #    'interactions_10_000.csv'
]

for p in paths:
    print("top video: ", get_top_video(p))
