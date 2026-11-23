
# Importar librerías
import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV
vehicles = pd.read_csv('vehicles_us.csv')

# Título y descripción de la aplicación
st.header('Dashboard de anuncios de vehículos')
st.write('Explora los datos de vehículos usados mediante gráficos interactivos.')

# Crear botón para el histograma
hist = st.checkbox('Construir histograma')

# Crear botón para el gráfico de dispersión
scatter = st.checkbox('Construir gráfico de dispersión')

# Si se presiona el botón del histograma
if hist:
    st.write('Distribución del kilometraje de los vehículos')

    fig = px.histogram(
        vehicles,
        x='odometer',
        title='Distribución del kilometraje',
        labels={
            'odometer': 'Kilometraje (km)',
            'Cantidad de vehículos': 'Cantidad de vehículos'
        }
    )

    st.plotly_chart(fig, use_container_width=True)

# Si se presiona el botón del gráfico de dispersión
if scatter:
    st.write('Relación entre kilometraje y precio')

    fig = px.scatter(
        vehicles,
        x='odometer',
        y='price',
        title='Kilometraje vs. precio',
        labels={
            'odometer': 'Kilometraje (km)',
            'price': 'Precio ($)'
        }
    )

    st.plotly_chart(fig, use_container_width=True)
