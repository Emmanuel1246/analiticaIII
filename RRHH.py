#@title conectar con google drive
from google.colab import drive
drive.mount('/content/drive')

#@title instalar sweetviz
!pip install sweetviz

import pandas as pd
import numpy as np
import sweetviz as sv
from datetime import datetime
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.express as px

#@title importar datos generales
bdg= pd.read_csv('/content/drive/MyDrive/Analitica III/Avance 1/general_data.csv',sep=';')
bdg.head()

#Verificación de columnas
bdg.columns

#Dimensiones de la BD
bdg.shape

#Tipos de variales en la BD
bdg.dtypes

#Convertir columnas a minuscula
bdg.columns= map(str.lower, bdg.columns)
bdg.head()

#Verificar nulos
bdg.isnull().sum()

#Copia de seguridad de BD
bdgcopy=bdg.copy()
bdgcopy

#reemplazar los nulos por 0, ya que todos los nulos se dan en numcompaniesworked y
#totalworkingyears entonces se pueden reemplazar los nulos por un 0 sin afectar la estructura 
bdgcopy=bdgcopy.fillna(0)

#volver a verificar nulos
bdgcopy.isnull().sum().sum()

#corroborar columna employeecount y standardhours, como todos tienen el valor 1 en el primer caso y 8 en el segundo pueden eliminarse las columnas
#ya que no aportan información relevante al modelo, también se elimina over18 ya que todos los empleados son mayores de edad
print(bdgcopy['employeecount'].unique())
print(bdgcopy['standardhours'].unique())
print(bdgcopy['over18'].unique())

bdgcopy=bdgcopy.drop(['employeecount'], axis=1)
bdgcopy=bdgcopy.drop(['standardhours'], axis=1)
bdgcopy=bdgcopy.drop(['over18'], axis=1)
bdgcopy.columns

bdgcopy.corr()

from matplotlib.pyplot import figure
import seaborn as sns
figure(figsize=(9,6), dpi = 80) # cambiar el tamaño de la grafica
sns.heatmap(bdgcopy.corr(), annot = True) # mapa de calor de las correlaciones

#bdgcopy.corr().unstack().sort_values().head(10)

#sns.pairplot(bdgcopy, height = 1.1, aspect=1.3, plot_kws ={'s':3})

reports = sv.analyze(bdgcopy)
reports.show_html(filepath='SWEETVIZ_REPORT.html', open_browser=True)


