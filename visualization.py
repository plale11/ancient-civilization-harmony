import matplotlib.pyplot as plt


def plot_food_storage(df):
    df["food_storage"].value_counts().plot(kind="bar")
    plt.title("Food Storage Systems in Early Civilizations")
    plt.xlabel("Storage Type")
    plt.ylabel("Count")
    plt.show()


def plot_community_structure(df):
    df["community_structure"].value_counts().plot(kind="bar")
    plt.title("Community Structures in Early Civilizations")
    plt.xlabel("Community Type")
    plt.ylabel("Count")
    plt.show()
