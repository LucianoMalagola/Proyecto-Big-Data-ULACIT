import pandas as pd
import os
from datetime import datetime

def log(message, log_lines):
    print(message)
    log_lines.append(message)

def limpiar_archivo(filepath, log_lines):
    """
    Limpia un archivo Excel:
    - Muestra y guarda en un log los valores faltantes y su ubicación
    - Forza la columna 'Código' a texto
    - Rellena valores faltantes con 0
    - Elimina filas completamente vacías
    - Guarda como <nombre>_limpio.xlsx en carpeta /limpieza
    """
    log(f"\nAnalizando: {filepath}", log_lines)
    df = pd.read_excel(filepath)

    # Forzar la columna 'Código' a texto si existe
    if 'Código' in df.columns:
        df['Código'] = df['Código'].astype(str)
        log("Columna 'Código' forzada a tipo texto.", log_lines)

    # Eliminar filas completamente vacías
    df = df.dropna(how='all')

    # Detectar valores faltantes antes de rellenar
    missing = df.isnull()
    total_missing = missing.sum().sum()

    if total_missing == 0:
        log("No se detectaron valores faltantes.", log_lines)
    else:
        log(f"Se detectaron {int(total_missing)} valores faltantes en:", log_lines)
        for row, col in zip(*missing.to_numpy().nonzero()):
            log(f"   → Fila {row+2}, Columna '{df.columns[col]}'", log_lines)

    # Rellenar valores faltantes con 0
    df = df.fillna(0)

    # Crear carpeta "limpieza" junto al archivo original
    dirpath, filename = os.path.split(filepath)
    limpieza_dir = os.path.join(dirpath, "limpieza")
    os.makedirs(limpieza_dir, exist_ok=True)

    # Construir nuevo nombre
    name, ext = os.path.splitext(filename)
    nuevo_nombre = os.path.join(limpieza_dir, f"{name}_limpio.xlsx")

    # Guardar limpio
    df.to_excel(nuevo_nombre, index=False)
    log(f"Archivo limpio guardado como: {nuevo_nombre}", log_lines)

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog

    # Crear interfaz para seleccionar archivos
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    filepaths = filedialog.askopenfilenames(
        title="Selecciona uno o más archivos Excel",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )

    if not filepaths:
        print("No se seleccionaron archivos.")
    else:
        log_lines = []
        limpieza_dir = None

        for filepath in filepaths:
            limpiar_archivo(filepath, log_lines)
            if limpieza_dir is None:
                # Usar la carpeta limpieza del primer archivo
                limpieza_dir = os.path.join(os.path.dirname(filepath), "limpieza")

        # Guardar el reporte en la carpeta limpieza con timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        reporte_path = os.path.join(
            limpieza_dir,
            f"reporte_limpieza_{timestamp}.txt"
        )
        with open(reporte_path, "w", encoding="utf-8") as f:
            f.write("\n".join(log_lines))

        print(f"\nProceso completado. Resumen guardado en: {reporte_path}")
