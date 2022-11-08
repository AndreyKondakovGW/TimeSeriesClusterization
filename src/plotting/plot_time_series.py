import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

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
    num_rows = (num_clusters + 1) // 2
    fig, axs = plt.subplots(nrows= num_rows, ncols=2, figsize=(20, num_rows * 5))
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

def plot_avg_timeseries_clusters(data, num_saples=100, num_clusters=10):
    num_rows = (num_clusters + 1) // 2
    fig, axs = plt.subplots(nrows= num_rows, ncols=2, figsize=(20, num_rows * 5))
    plt.subplots_adjust(hspace=0.5)
    fig.suptitle("Clusters", fontsize=18, y=0.95)

    for i, ax in enumerate(axs.ravel()):
        ax.set_title(f"Cluster {i}")
        cluster_data = data[data["cluster"] == i].iloc[:,:-1]
        if len(cluster_data) < num_saples:
            num_saples = len(cluster_data)
        for j in range(num_saples):
            ax.plot(cluster_data.iloc[j], linewidth=0.1, c="gray",alpha=0.7)
        ax.plot(cluster_data.mean(), linewidth=1.5, c="red")
        ax.set_xticks([])
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        ax.grid(True, which="both", axis="both")
    plt.show()

def plot_2d_clasters(data, clusters):
    plt.figure(figsize=(10, 10))
    plt.scatter(data[:,0], data[:,1], c=clusters)
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.grid(True, which="both", axis="both")
    plt.show()

def plot_3d_clasters(data, clusters):
    df = pd.DataFrame(data, columns=["PC1", "PC2", "PC3"])
    df["cluster"] = clusters
    fig = px.scatter_3d(df, x='PC1', y='PC2', z='PC3', color='cluster')
    fig.update_traces(marker_size = 2)
    fig.show()