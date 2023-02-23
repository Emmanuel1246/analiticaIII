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

# BD ENCUESTA DESEMPEÑO EMPLEADO -----------------------------------------------------------------------------
#@title importar datos generales
basedd = df= pd.read_csv("/content/drive/MyDrive/Analitica III/Avance 1/manager_survey_data.csv",sep = ",")
basedd.head()

#Verificación de columnas
basedd.columns

#Dimensiones de la BD
basedd.shape

#Tipos de variales en la BD
basedd.dtypes

#Convertir columnas a minuscula
basedd.columns= map(str.lower, basedd.columns)
basedd.head()

#Verificar nulos
basedd.isnull().sum()

#Copia de seguridad de BD
baseddcopy=basedd.copy()
baseddcopy

# crear dataset
# crear dataset
dic3 = base = basedd.groupby(['performancerating'])[['employeeid']].sum().sort_values('employeeid', ascending = False).reset_index()

# crear gráfica:
fig3 = px.pie(base, values = 'employeeid', names ='performancerating',
             title= '<b>Encuesta desempeño - clasificación de rendimiento<b>',
             color_discrete_sequence=px.colors.qualitative.G10)

# agregar detalles a la gráfica:
fig3.update_layout(
    xaxis_title = 'Año',
    yaxis_title = 'Precio de venta',
    template = 'simple_white',
    title_x = 0.5)

fig3.show()

# BD INFORMACION RETIRO EMPLEADOS -----------------------------------------------------------------------------

#@title importar datos generales
bdatar= pd.read_csv("/content/drive/MyDrive/Analitica III/Avance 1/retirement_info.csv",sep = ";")
bdatar.head()

#Verificación de columnas
bdatar.columns

#Dimensiones de la BD
bdatar.shape

#Tipos de variales en la BD
bdatar.dtypes

#Convertir columnas a minuscula
bdatar.columns= map(str.lower, bdatar.columns)
bdatar.head()

#Verificar nulos
bdatar.isnull().sum()

#Visualización de nulos
bdatar

# llenar valores con un valor particular, dado que en la columna está la opción "Others", los 70 nulos por el momento se dejan, para tratarlos mas adelante.
bdatar = bdatar.fillna("fired")

#Verificar nulos
bdatar.isnull().sum()

# crear dataset
dic = base = bdatar.groupby(['resignationreason'])[['employeeid']].sum().sort_values('employeeid', ascending = False).reset_index()
#base['resignationreason'] = base['resignationreason'].replace(dic)
# ExterQual: calidad del material del exterior del edificio

# crear gráfica:
fig = px.pie(base, values = 'employeeid', names ='resignationreason',
             title= '<b>Motivo de renuncia<b>',
             color_discrete_sequence=px.colors.qualitative.G10)

# agregar detalles a la gráfica:
fig.update_layout(
    xaxis_title = 'Año',
    yaxis_title = 'Precio de venta',
    template = 'simple_white',
    title_x = 0.5)

fig.show()

******************************************************************************

df1= pd.read_csv("/content/drive/MyDrive/Analitica III/Avance 1/employee_survey_data.csv",sep = ",")
dfd=df1.copy()

#Se miran los datos nulos de la base
dfd.isnull().sum()

# guardar la información en un diccionario para posteriormente usarla
diccionario = dfd[['EnvironmentSatisfaction','JobSatisfaction','WorkLifeBalance']].mean().round().to_dict()
diccionario

#Tratar los datos nulos
dfd = dfd[['EmployeeID','EnvironmentSatisfaction','JobSatisfaction','WorkLifeBalance']].fillna(diccionario)

based = dfd.groupby(['EnvironmentSatisfaction'])[['EmployeeID']].count().sort_values('EnvironmentSatisfaction').reset_index()

# crear gráfica
fig = px.pie(based,  values='EmployeeID',names= 'EnvironmentSatisfaction',
             title= '<b>Nivel de satisfacción del ambiente de trabajo<b>',
             color_discrete_sequence=px.colors.qualitative.G10)

# agregar detalles a la gráfica
fig.update_layout(
    xaxis_title = 'Nivel',
    yaxis_title = 'Cantidad de empleados',
    template = 'simple_white',
    title_x = 0.5)

fig.show()


basej = dfd.groupby(['JobSatisfaction'])[['EmployeeID']].count().sort_values('JobSatisfaction', ascending = False).reset_index()

# crear gráfica
figj = px.pie(basej, values='EmployeeID', names= 'JobSatisfaction',
             title= '<b>Nivel de satisfacción laboral<b>',
             color_discrete_sequence=px.colors.qualitative.G10)

# agregar detalles a la gráfica
figj.update_layout(
    xaxis_title = 'Nivel',
    yaxis_title = 'Cantidad de empleados',
    template = 'simple_white',
    title_x = 0.5)

figj.show()



basew = dfd.groupby(['WorkLifeBalance'])[['EmployeeID']].count().sort_values('WorkLifeBalance', ascending = False).reset_index()

# crear gráfica
figw = px.pie(basew, values='EmployeeID', names = 'WorkLifeBalance',
             title= '<b>Nivel de conciliación de la vida laboral y personal<b>',
             color_discrete_sequence=px.colors.qualitative.G10)

# agregar detalles a la gráfica
figw.update_layout(
    xaxis_title = 'Nivel',
    yaxis_title = 'Cantidad de empleados',
    template = 'simple_white',
    title_x = 0.5)

figw.show()






