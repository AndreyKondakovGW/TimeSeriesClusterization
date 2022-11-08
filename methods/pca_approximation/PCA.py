from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def get_pca_approximation(data, num_components=2):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    model = PCA(n_components=num_components)
    model.fit(scaled_data)
    return model.transform(data)

def get_pca_explained_variance_ratio(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    model = PCA()
    model.fit(scaled_data)
    return model.explained_variance_ratio_