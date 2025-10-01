#Importar librerias
import pandas as pd

#Cargar archivo CSV
data = pd.read_csv("dataset/XRPUSD_1m_Binance.csv")
df = pd.DataFrame(data)

# (Para este caso especial como son 3millones de valores trabajaremos con 50000 datos aleatorios)
df = df.sample(5000)

print(df)
#Tomar informacion de las columnas como el tipo de dato, info general y columnas con nulos
print("Tipo de valor:\n",df.dtypes,"\n")
print("Descripcion:\n",df.describe(),"\n")
print("Valores Nulos:\n", df.isnull().sum(),"\n")

#Llenar valores nulos con 0
df = df.fillna(0)

#Sustituir espacios de los nombres de las columnas
df.columns = df.columns.str.strip().str.replace(' ', '_')

#Tomar columnas del Dataset exepto Close_Time y Open Time para limpiar columnas numéricas de símbolos y convertir a float
columns = df.drop(columns=['Close_time','Open_time']).columns
for col in columns:
    if col in df.columns:
        df[col] = df[col].astype(str)
        df[col] = df[col].str.replace(r'[,%\-$\s]', '', regex=True).str.strip()
        df[col] = df[col].astype(float)

#Convertir las fechas a formato datetime
datetime = ['Close_time', 'Open_time'] 
df[datetime] = df[datetime].apply(pd.to_datetime, errors='coerce')

#Reordenar los indices del dataset por Datetime ascending
df = df.sort_values(by = 'Open_time', ascending=True).reset_index(drop=True)

#Check all changes have done correct
print(df.info())
print(df)

#Function to return dataframe en el app
def dataframe():
    return df


