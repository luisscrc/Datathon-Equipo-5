# Proyecto de Datathon Bosch 

Este proyecto se centra en analizar y comprender la deserción laboral en la planta de Bosch ubicada en Ciudad Juárez, Chihuahua. Utilizando un modelo de regresión logística, el proyecto busca identificar los factores clave que influyen en que un empleado permanezca en la empresa más tiempo que la media observada, que suele ser menor a cuatro años.


## Estructura del Proyecto

Descripción de la estructura del proyecto y qué contiene cada archivo o directorio.

- `Datathon 2-2.ipynb`: Análisis detallado y desarrollo del modelo para el datathon. **Aqui se desarrolla la limpieza de datos.**
- `README.md`: Información general y guía para este proyecto.
- `arbol_de_decision_antiguedad.ipynb`: Notebook con el modelo de árbol de decisión enfocado en la antigüedad. **Este es el archivo estrella de nuestro proyecto** pues es en est[a la interfaz de gradio funcional.
- `bosch_aic_datathon_limpio.csv`: Conjunto de datos limpio utilizado para análisis y modelado.
- `data/`: Datos originales en formato Excel.
- `data_sucia.csv`: Conjunto de datos inicial con un procesamiento minimo. Usado como checkpoint.
- `data_sucia_con_coordenadas.csv`: Datos originales enriquecidos con información de coordenadas.
- `distribucion_empleados.html`: Visualización de la distribución de los empleados. Este archivo es generado por Folium.
- `distribucion_empleados_mapa_calor.html`: Representación en mapa de calor de la distribución de empleados. Este archivo es generado por Folium.
- `flagged/`: Directorio que contiene logs y archivos marcados para revisión.
- `graficas.ipynb`: Notebook para la generación de gráficas relacionadas con el análisis de los datos tomando como punto de partida el archivo data_sucia_con_coordenadas.csv
- `modelo_regresionlog_motivos_renuncia.ipynb`: Modelo de regresión logística para analizar los motivos de renuncia.


## Participantes
- Luis Escarcega Corona
- Luis Guillermo Rodriguez Lopez
- Luis Adrian Garcia Acosta


## Tecnologías Utilizadas

Descripción de las tecnologías, lenguajes de programación y librerías utilizadas:

- Python: Lenguaje de programación principal.
- Pandas, NumPy: Para la manipulación y análisis de datos.
- Scikit-Learn: Para la construcción y evaluación de modelos de machine learning.
- Matplotlib, Seaborn: Para visualizaciones de datos.
- Gradio: Facilita la creación y compartición de interfaces de usuario para prototipos de modelos de machine learning, permitiendo demostraciones interactivas.
- Rapids: Suite de bibliotecas para ciencia de datos y machine learning en GPUs, proporcionando APIs similares a Pandas y Scikit-Learn con procesamiento acelerado.
- Plotly-Express: Biblioteca para gráficos interactivos y de alta calidad, permitiendo la creación de visualizaciones complejas con una sintaxis simple.
- Folium: Utilizada para la visualización de datos geoespaciales, facilita la creación de mapas interactivos en entornos Python y Jupyter Notebook.
- Anaconda: Distribución de Python y R para computación científica, que simplifica la gestión de paquetes y entornos para la ciencia de datos.

## Enlace a la conclusión en LaTEX


## Resultados del modelo
- Accuracy de 0.75. 

