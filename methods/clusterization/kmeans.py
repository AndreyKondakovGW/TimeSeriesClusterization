from sklearn.cluster import KMeans

def get_kmeans_clusters(data, num_clusters=10):
    model = KMeans(num_clusters)
    model.fit(data)
    return model.labels_

def elbow_method(data, max_num_clusters=10):
    sse = []
    for k in range(1, max_num_clusters):
        model = KMeans(k)
        model.fit(data)
        sse.append(model.inertia_)
    return sse