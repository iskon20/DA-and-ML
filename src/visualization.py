import matplotlib.pyplot as plt
import seaborn as sns


def subscription_pie(df, output):
    data = df["y"].value_counts()

    plt.figure(figsize=(6,6))
    plt.pie(data, labels=data.index, autopct="%1.1f%%")
    plt.title("Subscription to Term Deposit")

    plt.savefig(f"{output}/subscription_pie.png")
    plt.close()


def age_distribution(df, output):

    plt.figure(figsize=(8,5))
    sns.histplot(df["age"], bins=30)

    plt.title("Age Distribution of Clients")
    plt.xlabel("Age")
    plt.ylabel("Count")

    plt.savefig(f"{output}/age_distribution.png")
    plt.close()


def job_subscription_chart(df, output):

    job_sub = df.groupby(["job","y"]).size().unstack()

    job_sub.plot(kind="bar", figsize=(10,6))

    plt.title("Subscription by Job")
    plt.xlabel("Job")
    plt.ylabel("Clients")
    plt.xticks(rotation=45)

    plt.savefig(f"{output}/job_subscription.png")
    plt.close()


def balance_boxplot(df, output):

    plt.figure(figsize=(8,5))
    sns.boxplot(x=df["balance"])

    plt.title("Balance Distribution")

    plt.savefig(f"{output}/balance_boxplot.png")
    plt.close()


def correlation_matrix(df, output):

    numeric = df.select_dtypes(include=["int64","float64"])

    plt.figure(figsize=(8,6))
    sns.heatmap(numeric.corr(), annot=True)

    plt.title("Correlation Matrix")

    plt.savefig(f"{output}/correlation_matrix.png")
    plt.close()