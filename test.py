import seleccion
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge

documento = "Dataset/Dataset1.csv"
Data = []
target = []
Datos = []
class Regresion():
	def __init__(self):
		pass
	def lecturaDatos(self, Datos):
		Datos = pd.read_csv(Datos)
		Data = Datos[Datos.columns[0:-1]].as_matrix()
		target = Datos[Datos.columns[-1]].as_matrix()
		return 


print('Vacia: ', Data)
objeto = Regresion()
print('Esta es la dimensión de la matriz: ', objeto.lecturaDatos(documento))