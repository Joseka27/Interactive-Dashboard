#pip install pandas
#pip matplotlib
#pip install streamlit

#Importar librerias
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

#Cargar archivo CSV
data = pd.read_csv("dataset/XRPUSD_1m_Binance.csv")
df = pd.DataFrame(data)

# (Para este caso especial como son 3millones de valores trabajaremos con los primeros 50000)
df = df.head(50000)

print(df)
#Tomar informacion de las columnas como el tipo de dato, info general y columnas con nulos
print("Tipo de valor:\n",df.dtypes,"\n")
print("Descripcion:\n",df.describe(),"\n")
print("Valores Nulos:\n", df.isnull().sum(),"\n")

#Llenar valores nulos con 0
df = df.fillna(0)

#Sustituir espacios de los nombres de las columnas
df.columns = df.columns.str.strip().str.replace(' ', '_')

#Tomar columnas del Dataset exepto Close_Time y Open Time para eliminar valores como (, % - $)
columns = df.drop(columns=['Close_time','Open_time']).columns
for col in columns:
    if col in df.columns:
        df[col] = df[col].astype(str)
        df[col] = df[col].str.replace(r'[,%\-$\s]', '', regex=True).str.strip()
        df[col] = df[col].astype(float)

#Convertir las fechas a formato datetime
datetime = ['Close_time', 'Open_time'] 
df[datetime] = df[datetime].apply(pd.to_datetime, errors='coerce')

#Ordenar el dataset por Datetime ascending
df = df.sort_values(by = 'Open_time', ascending=True).reset_index(drop=True)

#Check all changes have done correct
print(df.info())
print(df)


