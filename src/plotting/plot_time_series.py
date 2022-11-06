import matplotlib.pyplot as plt

def plot_timeseries(data, title, num_series=100):
    plt.figure(figsize=(20, 5))
    plt.title(title)
    for i in range(num_series):
        plt.plot(data.iloc[i], linewidth=0.5)
    
    plt.xticks([])
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True, which="both", axis="both")
    plt.show()

def plot_timeseries_clusters(data, num_saples=100, num_clusters=10):
    fig, axs = plt.subplots(nrows=(num_clusters // 2) + 1, ncols=2, figsize=(20,((num_clusters // 2) + 1) * 5))
    plt.subplots_adjust(hspace=0.5)
    fig.suptitle("Clusters", fontsize=18, y=0.95)

    for i, ax in enumerate(axs.ravel()):
        ax.set_title(f"Cluster {i}")
        cluster_data = data[data["cluster"] == i].iloc[:,:-1]
        if len(cluster_data) < num_saples:
            num_saples = len(cluster_data)
        for j in range(num_saples):
            ax.plot(cluster_data.iloc[j], linewidth=0.5)
        ax.set_xticks([])
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        ax.grid(True, which="both", axis="both")
    plt.show()
