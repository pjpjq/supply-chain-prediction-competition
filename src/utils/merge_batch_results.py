import pandas as pd
import glob


def merge_batch_results(csvs_dir="../../batch-results/", out_name="../../merged.csv"):
    interesting_files = glob.glob(csvs_dir + "*.csv")
    print(len(interesting_files))
    df = pd.concat((pd.read_csv(f, header=0) for f in interesting_files))
    df.describe()
    df.to_csv(out_name, index=False)


if __name__ == '__main__':
    merge_batch_results()
