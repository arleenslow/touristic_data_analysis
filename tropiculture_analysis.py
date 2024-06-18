# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar las tablas desde archivos Excel
reservas = pd.read_excel('Reservas_de_Viajes.xlsx')
tours = pd.read_excel('Tours_Organizados.xlsx')

# Limpieza de Datos

# Verificar duplicados
reservas_duplicates = reservas[reservas.duplicated()]
tours_duplicates = tours[tours.duplicated()]

# Eliminar duplicados si existen
reservas = reservas.drop_duplicates()
tours = tours.drop_duplicates()

# Convertir columnas de fechas a datetime
reservas['Fecha de Reserva'] = pd.to_datetime(reservas['Fecha de Reserva'])
tours['Date'] = pd.to_datetime(tours['Date'])

# Asegurar que los campos numéricos estén correctamente tipificados
reservas['Número de Personas'] = reservas['Número de Personas'].astype(int)
reservas['Duración del Viaje'] = reservas['Duración del Viaje'].astype(int)
reservas['Costo del Viaje'] = reservas['Costo del Viaje'].astype(float)

tours['Duration (days)'] = tours['Duration (days)'].astype(int)
tours['Participants'] = tours['Participants'].astype(int)

# Análisis Exploratorio de Datos (EDA)

# Estadísticas descriptivas
reservas_stats = reservas[['Duración del Viaje', 'Número de Personas', 'Costo del Viaje']].describe()
tours_stats = tours[['Duration (days)', 'Participants']].describe()

# Gráficos

# Distribución de destinos
plt.figure(figsize=(10, 6))
sns.countplot(y='Destino del Viaje', data=reservas, order=reservas['Destino del Viaje'].value_counts().index)
plt.title('Distribución de Destinos')
plt.show()

# Distribución de tipos de experiencias
plt.figure(figsize=(10, 6))
sns.countplot(y='Tipo de Experiencia', data=reservas, order=reservas['Tipo de Experiencia'].value_counts().index)
plt.title('Distribución de Tipos de Experiencias')
plt.show()

# Estado de pago
plt.figure(figsize=(8, 6))
reservas['Estado de Pago'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Distribución de Estados de Pago')
plt.ylabel('')
plt.show()

# Guías principales
plt.figure(figsize=(10, 6))
sns.countplot(y='Lead Guide', data=tours, order=tours['Lead Guide'].value_counts().index)
plt.title('Distribución de Guías Principales')
plt.show()

# Análisis de Correlación

# Relación entre el costo del viaje y el número de personas
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Número de Personas', y='Costo del Viaje', data=reservas)
plt.title('Relación entre el Costo del Viaje y el Número de Personas')
plt.show()

# Relación entre la duración del viaje y el estado de pago
plt.figure(figsize=(10, 6))
sns.boxplot(x='Estado de Pago', y='Duración del Viaje', data=reservas)
plt.title('Relación entre la Duración del Viaje y el Estado de Pago')
plt.show()

# Relación entre destino y tipo de experiencia más reservada
plt.figure(figsize=(12, 8))
sns.countplot(x='Destino del Viaje', hue='Tipo de Experiencia', data=reservas)
plt.title('Relación entre Destino del Viaje y Tipo de Experiencia Más Reservada')
plt.xticks(rotation=45)
plt.show()

# Visualización de Datos

# Evolución temporal de las reservas
plt.figure(figsize=(12, 6))
reservas.set_index('Fecha de Reserva').resample('M').size().plot()
plt.title('Evolución Temporal de las Reservas')
plt.xlabel('Fecha')
plt.ylabel('Número de Reservas')
plt.show()

# Evolución temporal de los tours
plt.figure(figsize=(12, 6))
tours.set_index('Date').resample('M').size().plot()
plt.title('Evolución Temporal de los Tours')
plt.xlabel('Fecha')
plt.ylabel('Número de Tours')
plt.show()

# Mapa de distribución geográfica de los destinos turísticos
# Nota: Este paso requiere instalación y configuración de geopandas y shapely para crear mapas interactivos.


