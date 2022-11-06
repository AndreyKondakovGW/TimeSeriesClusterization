from pandas import DataFrame
from scipy.optimize import curve_fit
import numpy as np

def get_dummy_approximation(data, num_periods=100):
    approximation = data.iloc[:,::len(data) // num_periods]
    approximation[data.columns[-1]] = data.iloc[:,-1]
    return approximation

def get_linearmean_approximation(data, num_periods=100):
    approximation = DataFrame()
    period_size = len(data.columns) // num_periods
    for i in range(num_periods):
        approximation[str(i*period_size + period_size // 2)] = data.iloc[:,i*period_size:(i+1)*period_size].mean(axis=1)
    approximation[data.columns[-1]] = data.iloc[:,-1]
    return approximation

def piecewise_linear(x, x0, y0, k1, k2):
    return np.piecewise(x, [x < x0, x >= x0], [lambda x:k1*x + y0-k1*x0, lambda x:k2*x + y0-k2*x0])

def get_pla_approximation(data, num_periods=100):
    x = np.array(data.columns, dtype=float)
    period_size = len(x) // num_periods
    res = np.empty((len(data), num_periods), dtype=float)
    for index, row in data.iterrows():
        y = row.values
        for i in range(num_periods):
            p , e = curve_fit(piecewise_linear, x[i*period_size:(i+1)*period_size], y[i*period_size:(i+1)*period_size], maxfev = 5000)
            res[index][i] = piecewise_linear(np.array([x[i*period_size + period_size // 2]]), *p)
    approximation = DataFrame(res, columns=[str(i*period_size + period_size // 2) for i in range(num_periods)])
    approximation[data.columns[-1]] = data.iloc[:,-1]
    approximation[data.columns[0]] = data.iloc[:,0]


    cols = approximation.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    approximation = approximation[cols]
    return approximation
