# TimeSeriesClusterization
Репозиторий посвящён обзору и сравнению методов кластеризации временных рядов, а также имплементации данных методов  

-- 

**Данные**
Для тестирования используется набор данных отсюда: https://www.kaggle.com/datasets/passwordclassified/synthesised-time-series-data


**Методы**
На данный момент рассмотрены методы:
* Апроксимации, для понижения размерности временных рядов: [notebook](methods/lin_approximation/test_synthesis.ipynb)

* Понижения размерности с помощью метода главных компонент: [notebook](methods/pca_approximation/test_synthesis.ipynb)

* Сравнения использования данных методов совместно с алгоритмом кластеризации kmean: [notebook](methods/test_kmean.ipynb)
