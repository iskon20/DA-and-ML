from load_data import load_dataset
from analysis import basic_info
import visualization as viz
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "bank-full.csv"
OUTPUT_PATH = BASE_DIR / "output"


def main():

    df = load_dataset(DATA_PATH)

    basic_info(df)

    viz.subscription_pie(df, OUTPUT_PATH)
    viz.age_distribution(df, OUTPUT_PATH)
    viz.job_subscription_chart(df, OUTPUT_PATH)
    viz.balance_boxplot(df, OUTPUT_PATH)
    viz.correlation_matrix(df, OUTPUT_PATH)

    print("All graphs saved to output folder")


if __name__ == "__main__":
    main()