def basic_info(df):
    print(df.info())
    print(df.describe())


def subscription_stats(df):
    return df["y"].value_counts()


def job_subscription(df):
    return df.groupby(["job", "y"]).size().unstack()