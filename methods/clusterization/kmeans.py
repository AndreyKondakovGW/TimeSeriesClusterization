from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def get_kmeans_clusters(data, num_clusters=10):
    model = KMeans(num_clusters)
    model.fit(data)
    return model.labels_

def elbow_method(data, max_num_clusters=10):
    sse = []
    for k in range(2, max_num_clusters):
        model = KMeans(k)
        model.fit(data)
        sse.append(model.inertia_)
    return sse

def silhouette_method(data, max_num_clusters=10):
    silhouette_scores = []
    for k in range(2, max_num_clusters):
        model = KMeans(k)
        model.fit(data)
        silhouette_scores.append(silhouette_score(data, model.labels_))
    return silhouette_scores