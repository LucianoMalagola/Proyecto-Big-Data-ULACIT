# Proyecto-Big-Data-ULACIT
Proyecto para el curso “Big Data y Tecnologías de la Información” de ULACIT. ETL de datos de ventas con limpieza en Python, consolidación en Power Query y preparación para un análisis predictivo. Objetivo: optimización de inventarios, análisis predictivo de ventas y comparación de varianza de ventas entre 2024 y 2025.

# Proyecto para el curso "Big Data y Tecnologías de la Información"

## Integrantes del Grupo
- Carolina Mena - Investigación Académica y Soporte en Análisis
- Karol Montero Ulate – Analista de Ventas y Estrategias de Inventario  
- Luciano Malagola Angola - Desarrollador de ETL y Visualización de Datos 
- María Fernanda Salas - Investigación Académica con Enfoque en Análisis de Ventas
- Maritza Cruz Díaz - Investigación Académica y Búsqueda de Soluciones Basadas en Big Data

## Contenido del Repositorio
- `1. datos_originales`: Incluye archivos de Excel con los datos previos al proceso ETL de los primeros cinco meses de 2025.
- `2. script_limpieza.python`: Incluye script en Python para la limpieza inicial de los datos.
- `3. proyecto_powerbi_query`: Incluye archivo de Power BI con la preparación del conjunto de datos consolidado usando Power Query
- `4. datos_consolidados_post_ETL`: Incluye archivo de Excel con los datos limpios, estandarizados y consolidados (post proceso ETL).
- `5. dashboard_powerbi`: Incluye el archivo descargable del Dashboard Interactivo en Power BI y su versión en PDF para revisión rápida.
- `README.md`: Este documento.

## Proceso ETL

1️. **Extracción**  
Los conjuntos de datos utilizados son reportes que se descargan del sistema de ventas de inventario que utilizan las tiendas estudiadas.

2️. **Transformación**  
- Conversión de la columna `Código` a texto.
- Reemplazo de valores nulos por `0`.
- Eliminación de filas vacías.
- Estandarización de nombres de columnas y eliminación de columnas innecesarias.
- Creación de columnas `Mes`, `MesNúmero` y `Total Ventas` para análisis cronológico.

3️. **Carga**  
Los datos consolidados se exportaron a un archivo único `BD_meses_consolidados.xlsx`, listo para su análisis, visualización y uso en el entrenamiento de un modelo de predicción.

## Herramientas utilizadas

- **Python** (pandas, matplotlib, seaborn) — para la limpieza inicial.
- **Power Query** (Power BI) — para la consolidación y estandarización final.
- **Power BI** — para el análisis y visualización de los datos
