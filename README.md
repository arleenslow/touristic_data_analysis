### Análisis de Reservas y Tours en el Sector Turístico de Colombia

#### Objetivo del Proyecto:
Analizar las reservas y tours organizados en diversos destinos turísticos en Colombia. Se busca identificar patrones y tendencias en las reservas y tours, 
como la popularidad de los destinos, la duración de los viajes, el número de participantes y la relación entre el costo del viaje y el estado de pago. 
Esto ayudará a la agencia turística a optimizar sus ofertas y mejorar la experiencia del cliente.

#### Pasos del Proyecto:

1. **Importación de Datos:**
   - Importar las dos tablas en una herramienta de análisis de datos como Excel, Google Sheets, o un entorno de programación como Python (pandas).
   
2. **Limpieza de Datos:**
   - Verificar que no haya datos duplicados o erróneos.
   - Asegurar que las fechas estén en el formato correcto y que los campos numéricos (costo, duración, participantes) estén correctamente tipificados.

3. **Análisis Exploratorio de Datos (EDA):**
   - Calcular estadísticas descriptivas (promedios, medianas, desvíos estándar) para variables como la duración del viaje, número de personas, costo del viaje y número de participantes.
   - Crear gráficos de barras y pasteles para visualizar la distribución de destinos, tipos de experiencias, estados de pago y guías principales.

4. **Análisis de Correlación:**
   - Evaluar la relación entre el costo del viaje y el número de personas, así como la duración del viaje.
   - Analizar la correlación entre la duración del viaje y el estado de pago.
   - Investigar si hay una relación entre el destino del viaje y el tipo de experiencia más reservada.

5. **Conclusiones y Recomendaciones:**
   - Identificar los destinos más populares y los menos solicitados.
   - Determinar la duración promedio de los viajes y tours y su relación con el costo.
   - Proponer estrategias para mejorar la tasa de pago de las reservas pendientes.
   - Sugerir nuevos tipos de experiencias o mejorar las existentes basado en la demanda observada.


### Informe de Análisis de Datos

#### Limpieza de Datos
Se verificó que no haya datos duplicados ni erróneos en las tablas proporcionadas. Se convirtió las columnas de fechas al formato datetime y se aseguraron los tipos correctos para los campos numéricos.

#### Análisis Exploratorio de Datos (EDA)
- **Estadísticas descriptivas**: Se calcularon las estadísticas descriptivas para las variables de duración del viaje, número de personas, costo del viaje y número de participantes en los tours. Los resultados muestran que:
  - La duración promedio de los viajes es de 4 días, con un rango de 2 a 7 días.
  - El número promedio de personas por reserva es de 3, con un rango de 1 a 6.
  - El costo promedio del viaje es de aproximadamente 2600 USD.
  - El número promedio de participantes por tour es de 11.

- **Distribución de destinos**: Los destinos más populares son Cartagena, Medellín y Bogotá.
- **Distribución de tipos de experiencias**: Las experiencias culturales y los tours gastronómicos son los más solicitados.
- **Estado de pago**: Aproximadamente el 70% de las reservas están pagadas, un 20% están pendientes y un 10% han sido canceladas.
- **Guías principales**: Los guías más activos son Laura García y Pedro García.

#### Análisis de Correlación
- **Costo del viaje y número de personas**: Existe una relación positiva entre el costo del viaje y el número de personas. A medida que aumenta el número de personas, también lo hace el costo del viaje.
- **Duración del viaje y estado de pago**: No se observó una relación clara entre la duración del viaje y el estado de pago.
- **Destino del viaje y tipo de experiencia más reservada**: Los destinos como Cartagena y San Andrés están más asociados a experiencias gastronómicas y de buceo, respectivamente.

#### Conclusiones y Recomendaciones
1. **Destinos Populares**: Cartagena, Medellín y Bogotá son los destinos más populares. Se recomienda aumentar la oferta de experiencias en estos destinos para captar mayor demanda.
2. **Duración y Costo de los Viajes**: La duración promedio de los viajes es de 4 días y el costo promedio es de 2600 USD. Se puede considerar ofrecer paquetes promocionales para estadías más largas o descuentos para grupos grandes.
3. **Mejora de la Tasa de Pago**: Se sugiere implementar recordatorios automáticos de pago y ofrecer opciones de pago en cuotas para reducir el número de reservas pendientes.
4. **Nuevas Experiencias**: Basado en la demanda, se pueden desarrollar nuevas experiencias culturales y gastronómicas, así como promocionar actividades de ecoturismo y aventura en destinos menos populares.
