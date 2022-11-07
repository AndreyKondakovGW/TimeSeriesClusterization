from tslearn.utils import to_time_series_dataset
from tslearn.clustering import TimeSeriesKMeans

def get_tslearn_kmean_clusters(data, num_clusters=10, metric = "dtw", num_init=10, max_iter=300, random_state=42):
    time_series_data = to_time_series_dataset(data.values)
    kmean = TimeSeriesKMeans(n_clusters=num_clusters,metric=metric, n_init=num_init, max_iter=max_iter, random_state=random_state)
    labels = kmean.fit_predict(time_series_data)
    return labels

def elbow_tslearn_method(data, max_num_clusters=10, metric = "dtw", num_init=10, max_iter=300, random_state=42):
    time_series_data = to_time_series_dataset(data.values)
    sse = []
    for k in range(2, max_num_clusters):
        kmean = TimeSeriesKMeans(n_clusters=k,metric=metric, n_init=num_init, max_iter=max_iter, random_state=random_state)
        kmean.fit(time_series_data)
        sse.append(kmean.inertia_)
    return sse

def silhouette_tslearn_method(data, max_num_clusters=10, metric = "dtw", num_init=10, max_iter=300, random_state=42):
    time_series_data = to_time_series_dataset(data.values)
    silhouette_scores = []
    for k in range(2, max_num_clusters):
        kmean = TimeSeriesKMeans(n_clusters=k,metric=metric, n_init=num_init, max_iter=max_iter, random_state=random_state)
        kmean.fit(time_series_data)
        silhouette_scores.append(kmean.inertia_)
    return silhouette_scores