# Proyecto-Big-Data-ULACIT
Proyecto para el curso “Big Data y Tecnologías de la Información” de la ULACIT. ETL de datos de ventas con limpieza en Python, consolidación en Power Query y preparación para un modelo predictivo. Objetivo: optimización de inventarios y predicción de ventas con Big Data.


# Proyecto para el curso "Big Data y Tecnologías de la Información" - ULACIT

## Integrantes del Grupo
- Carolina Mena  
- Karol Montero Ulate  
- Luciano Malagola Angola  
- María Fernanda Salas  
- Maritza Cruz Díaz 

## Contenido del Repositorio
- `1. datos_originales/`: Incluye archivos de Excel con los datos previos al proceso ETL de los primeros cinco meses de 2025.
- `2. script_limpieza.python/`: Incluye script en Python para la limpieza inicial de los datos.
- `3. proyecto_powerbi_query`: Incluye archivo de Power BI con la preparación del conjunto de datos consolidado usando Power Query
- `4. datos_consolidados_post_ETL/`: Incluye archivo de Excel con los datos limpios, estandarizados y consolidados (post proceso ETL).
- `README.md`: Este documento.

## Proceso ETL

1️⃣ **Extracción**  
Los conjuntos de datos utilizados son reportes que se descargan del sistema de ventas de inventario que utilizan las tiendas estudiadas.

2️⃣ **Transformación**  
- Conversión de la columna `Código` a texto.
- Reemplazo de valores nulos por `0`.
- Eliminación de filas vacías.
- Estandarización de nombres de columnas y eliminación de columnas innecesarias.
- Creación de columnas `Mes`, `MesNúmero` y `Total Ventas` para análisis cronológico.

3️⃣ **Carga**  
Los datos consolidados se exportaron a un archivo único `BD_meses_consolidados.xlsx`, listo para análisis y visualización en Power BI.

## Herramientas utilizadas

- **Python** (pandas, matplotlib, seaborn) — para la limpieza inicial y posteriormente para la elaboración del modelo de predicción.
- **Power Query** (Power BI) — para la consolidación y estandarización final.
- **Power BI** — para el análisis y visualización de los datos
- **Google Colab** ' para el desarrollo del modelo de predicción utilizando Python y librerías
