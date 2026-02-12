# Machine Learning Final Project

Este es el proyecto final de nuestro bootcamp de Machine Learning, donde demostramos las habilidades y conocimientos adquiridos a lo largo de nuestros estudios. A lo largo de este bootcamp, hemos estudiado diferentes modelos basados en proyectos de diferentes áreas y tipos. Ahora es el momento de crear nuestro propio proyecto utilizando el algoritmo que creemos que se adapta mejor a nuestro problema.

Tendremos que encontrar un conjunto de datos adecuado para trabajar, procesarlo, entrenar un modelo y, finalmente, ponerlo a disposición para su consumo.

> *"Hard work always beats talent when talent doesn't work hard"* - Tim Notke

## 👥  Credits

**Team Members:**
> - Rodolfo 
> - Eder
> - Gregoriant

**Academy:** 
> - [4Geeks Academy](https://4geeksacademy.com/us/index) 
> - **Bootcamp:** Spain-DS-17 
> - **Mentor:** [Ing. Héctor Chocobar Torrejón](https://github.com/hchocobar/)
> - **Teacher Assitant:** [Beatriz Solana Ros](https://github.com/mezcolantriz)

## 🎯 Project Goal

Proyecto de Crime predict
Objetivo del proyecto:
 Queremos crear un filtro de seguridad para aplicaciones inmobiliarias que permita a los usuarios ver cuán segura es una zona antes de decidir alquilar o comprar una vivienda. Esto se basa en datos de criminalidad de los municipios de unas provincias en Espana (Madrid, Barcelona, Valencia, Alicante, Castellon).



El objetivo de este proyecto es desarrollar una solución completa de Machine Learning de extremo a extremo que incluya:

- Adquisición y procesamiento de datos
- Análisis exploratorio de datos (EDA)
- Desarrollo y optimización de modelos
- Desarrollo de aplicaciones Web
- Resolución de problemas del mundo real a través de técnicas de ML

### Dataset
Datos que vamos a usar:
Dataset del Ministerio del Interior: criminalidad por municipios de la Comunidad de Madrid, trimestral (cada trimestre muestra los delitos ocurridos en ese periodo). Categorías de delitos: homicidios, robos, hurtos, tráfico de drogas, daños, entre otros.
https://estadisticasdecriminalidad.ses.mir.es/publico/portalestadistico/balances

Dataset de la poblacion de cada municipio. https://ine.es/


### Methodology
* Importación de librerías y cargado de dataset

* Análisis inicial de estructura de dataframe, tipo de variables y calidad

* Limpieza de datos nulos, duplicados, vacíos y outliers

* Renombrado y orden de columnas

* Transformaciones de columnas: nuevas columnas y asignaciones grupales

* Análisis Exploratorio (EDA)

* Visualizaciones

* Guardado de resultados y observaciones del análisis

* Normalización, encoding de datos y separación train/test

* Creación y prueba de distintos modelos

* Entrenamiento de modelo

* Hiperparametrización del modelo

* Calculo de precisión y errores


## 📁 Project Structure
```
SP-ML-20-FINAL-PROJECT-G4/
├── data/
│   ├── processed/         # Datos procesados (población y modelado) [1]
│   └── raw/               # Datos originales (Barcelona, Madrid, etc.) [1]
├── database/              # Almacenamiento de base de datos [1]
├── docs/                  # Documentación técnica adicional [1]
├── models/                # Modelos entrenados (.pkl) [2]
│   ├── modelo_alicante.pkl
│   ├── modelo_barcelona.pkl
│   ├── modelo_castellon.pkl
│   ├── modelo_madrid.pkl
│   └── modelo_valencia.pkl
├── notebooks/             # Notebooks de experimentación [1]
├── src/                   # Scripts principales del proyecto [1]
│   ├── 01_crimenes_datos.ipynb
│   ├── 02_poblacion_datos.ipynb
│   ├── 03_analisis_visualizacion.ipynb
│   └── 04_preparacion_series_temporales.ipynb
├── webapp/                # Archivos de la aplicación web [1]
└── README.md              # Archivo de documentación actual [1]
```

## 🛠️ Technologies Used

- Python 3.10.11
- numpy, pandas, scikit-learn, Sarimax, streamlit, entre otras librerías.
- Jupyter Notebooks para análisis y experimentación.
- Streamlit para despliegue web interactivo.
