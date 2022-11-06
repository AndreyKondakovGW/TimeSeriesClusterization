from sklearn.preprocessing import MinMaxScaler

def scale_data(data, scaler=None):
    scale_data = data.copy()
    if scaler is None:
        scaler = MinMaxScaler()

    for i in range(len(scale_data)):
        scale_data.iloc[i] = scaler.fit_transform(scale_data.iloc[i].values.reshape(-1, 1)).reshape(-1)
    
    return scale_data