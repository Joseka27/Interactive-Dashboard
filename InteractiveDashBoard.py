#Importar librerias
from CleanData import dataframe #importar el dataframe limpio
import streamlit as st
from datetime import date

df = dataframe()

#Configuracion de la pestaña de la pagina
st.set_page_config(
    page_title="Proyecyto Dashboar Interactivo", 
    page_icon=":bar_chart:", layout="wide",)

#Establecer titulo y descripcion
"""
# Proyecto Dashboard Interactivo
Este es un proyecto de un dashboard interactivo donde se analizan datos de la criptomoneda XRP
"""

#Dividir la hoja en 3 partes (visual)
cols = st.columns([1,3])

#Establecer contenedores de los diagramas y botones
top_left_cell = cols[0].container(
    border=True, height="stretch", vertical_alignment="center"
)
right_cell = cols[1].container(
    border=True, height="stretch", vertical_alignment="center"
)
bottom_left_cell = cols[0].container(
    border=True, height="stretch", vertical_alignment="center"
)

#Diccionarios para los botones de Año
Actual_Date = date.today()
Actual_Year = Actual_Date.year

Year_select = {}
for year in range(Actual_Year - 10, Actual_Year + 1):
    Year_select[str(year)] = str(year)
#Diccionario para el selector de Mes
Month_select = {
    "Enero": '01',
    "Febrero": '02',
    "Marzo": '03',
    "Abril": '04',
    "Mayo": '05',
    "Junio": '06',
    "Julio": '07',
    "Agosto": '08',
    "Septiembre": '09',
    "Octubre": '10',
    "Noviembre": '11',
    "Diciembre": '12',
}

#Boton para seleccionar el Año
with top_left_cell: #Esta linea acomoda en el contenedor
    year = st.pills(
        "Seleccionar Año",
        options=list(Year_select.keys()),
        default="2025",
    )

#Seleccion para el Mes
with top_left_cell: #Esta linea acomoda en el contenedor
    months = st.multiselect(
    "Seleccionar Mes",
    options=list(Month_select.keys()),
    default=["Enero"],
    placeholder="Escoge un Mes",
)

#Realizar una copia del dataframe para filtrar por año y mes
df_filtered = df.copy()
if year and year != "Todos":  # verificar que año tenga valor
    df_filtered = df_filtered[df_filtered["Open_time"].dt.year == int(year)]
if months:
    selected_months = [int(Month_select[m]) for m in months]
    df_filtered = df_filtered[df_filtered["Open_time"].dt.month.isin(selected_months)]

#Grafica de linea del precio del la moneda por fecha
with right_cell:
    st.line_chart(
        df_filtered,
        x="Open_time",
        y="Close",
        x_label="Fecha",
        y_label="Precio (USD)",
        use_container_width=True,
        height=500,
        color="#FF0000",
    )

#Mostrar los valores mas altos y mas bajos de la seleccion, mostrando su porcentaje de cambio
with bottom_left_cell:
    cols = st.columns(2)
    
    if not df_filtered.empty:
        #Precio más alto y más bajo
        high_price = df_filtered["High"].max()
        low_price = df_filtered["Low"].min()
        
        #Calcular precio inicial y final del mes seleccionado
        first_price = df_filtered["Close"].iloc[0]
        last_price = df_filtered["Close"].iloc[-1]
        
        #Porcentaje de cambio
        pct_change = ((last_price - first_price) / first_price) * 100
        
        #Mostrar Precio más alto con % cambio
        cols[0].metric(
            "Precio más alto",
            f"${high_price:,.4f}",
            delta=f"{pct_change:+.2f}%"
        )
        
        #Mostrar Precio más bajo con % cambio
        cols[1].metric(
            "Precio más bajo",
            f"${low_price:,.4f}",
            delta=f"{pct_change:+.2f}%"
        )
    else:
        #En caso de que no haya datos para la seleccion
        cols[0].metric("Precio más alto", "N/A", delta="N/A")
        cols[1].metric("Precio más bajo", "N/A", delta="N/A")
    
#Mostrar datos en dataframe filtrado
st.dataframe(df_filtered)

#Redes sociales para dar retro alimentacion
st.markdown(
    """
    <h1> Dar quieres dar retro alimentacio</h1>
    <p>
    <a href="https://twitter.com/lilJoseka" target="_blank" style="text-decoration:none; display:inline-flex; align-items:center; margin-right:20px;">
        <img src="https://cdn-icons-png.flaticon.com/24/733/733579.png" width="40" style="vertical-align:middle; margin-right:30px;">
        @lilJoseka
    </a>
    <a href="https://www.linkedin.com/in/josecubero12/" target="_blank" style="text-decoration:none; display:inline-flex; align-items:center; margin-right:20px;">
        <img src="https://cdn-icons-png.flaticon.com/24/174/174857.png" width="40" style="vertical-align:middle; margin-right:30px;">
        @josecubero12
    </a>
    <a href="https://github.com/Joseka27" target="_blank" style="text-decoration:none; display:inline-flex; align-items:center;">
        <img src="https://cdn-icons-png.flaticon.com/24/25/25231.png" width="40" style="vertical-align:middle; margin-right:30px;">
        @Joseka27
    </a>
    </p>
    """,
    unsafe_allow_html=True
)