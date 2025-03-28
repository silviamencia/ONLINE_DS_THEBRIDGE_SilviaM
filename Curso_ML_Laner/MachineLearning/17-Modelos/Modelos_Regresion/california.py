# -*- coding: utf-8 -*-
# https://www.datatechnotes.com/2020/10/regression-example-with-decisiontreeregressor.html#:~:text=Scikit-learn%20API%20provides%20the%20DecisionTreeRegressor%20class%20to%20apply,data%20by%20using%20the%20DecisionTreeRegressor%20class%20in%20Python.

from sklearn.tree import DecisionTreeRegressor
#from sklearn.datasets import load_boston
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
from sklearn import set_config

from sklearn.datasets import fetch_california_housing
# genera un conjunto de datos artificial
x, y = make_regression(n_samples=5000, n_features=10)
print(x[0:2])
print(y[0:2])

x = scale(x)
y = scale(y)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=.10)

# mostrar todos los parametros del estimador aunque no hayan sido modificados
set_config(print_changed_only=False)

dtr = DecisionTreeRegressor()
print(dtr)

dtr.fit(xtrain, ytrain)

score = dtr.score(xtrain, ytrain)
print("R-squared:", score)

ypred = dtr.predict(xtest)

mse = mean_squared_error(ytest, ypred)
print("MSE: ", mse)
print("RMSE: ", mse**(1/2.0))


x_ax = range(len(ytest))
plt.plot(x_ax, ytest, linewidth=1, label="original")
plt.plot(x_ax, ypred, linewidth=1.1, label="predicted")
plt.title("y-test and y-predicted data")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc='best',fancybox=True, shadow=True)
plt.grid(True)
plt.show()



###########################################################################################




from sklearn.datasets import fetch_california_housing

# información sobre factores que afectan los precios de las viviendas en California
# variable objetivo: precio promedio de las casas en cada vecindario
print("California housing dataset prediction.")
california = fetch_california_housing(as_frame=True)
x, y = california.data, california.target

print(x.shape)
print(y.shape)

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.15, random_state=42)

dtr = DecisionTreeRegressor()
dtr.fit(xtrain, ytrain)

score = dtr.score(xtrain, ytrain)
print("R-squared:", score)

ypred = dtr.predict(xtest)
mse = mean_squared_error(ytest, ypred)
print("MSE: ", mse)
print("RMSE: ", mse**(1/2.0))
score = dtr.score(xtest, ytest)
print("R-squared:", score)

print(y.min())
print(y.max())

# Visualizar las predicciones
x_ax = range(len(ytest))
plt.plot(x_ax, ytest, label="original")
plt.plot(x_ax, ypred, label="predicted")
plt.title("California test and predicted data")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc='best', fancybox=True, shadow=True)
plt.grid(True)
plt.show()


# graficamos solo los primeros 200 puntos para visualizar mejor
x_ax = range(200)
plt.plot(x_ax, ytest[:200], label="original")
plt.plot(x_ax, ypred[:200], label="predicted")
plt.title("California test and predicted data (subset)")
plt.xlabel('Sample index')
plt.ylabel('Scaled target')
plt.legend(loc='best', fancybox=True, shadow=True)
plt.grid(True)
plt.show()




